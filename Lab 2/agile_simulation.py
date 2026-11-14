"""
Lab 2: Agile Backlog Creation & Sprint Simulation in Jira
Software Engineering (UE24CS351A)
Student SRN: PES1UG24CS387
Domain: Plate Pilot (Healthcare & Telemedicine Dietary Management System)
"""

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Dict, Optional


class Priority(Enum):
    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


class IssueStatus(Enum):
    TO_DO = "To Do"
    IN_PROGRESS = "In Progress"
    DONE = "Done"


@dataclass
class UserStory:
    story_id: str
    epic_id: str
    title: str
    as_a: str
    i_want: str
    so_that: str
    story_points: int
    priority: Priority
    acceptance_criteria: List[str]
    status: IssueStatus = IssueStatus.TO_DO
    completed_day: Optional[int] = None

    def move_to(self, new_status: IssueStatus, day: Optional[int] = None):
        self.status = new_status
        if new_status == IssueStatus.DONE:
            self.completed_day = day


@dataclass
class Epic:
    epic_id: str
    title: str
    description: str
    user_stories: List[UserStory] = field(default_factory=list)

    @property
    def total_story_points(self) -> int:
        return sum(s.story_points for s in self.user_stories)

    @property
    def completed_story_points(self) -> int:
        return sum(s.story_points for s in self.user_stories if s.status == IssueStatus.DONE)

    @property
    def progress_percentage(self) -> float:
        if self.total_story_points == 0:
            return 0.0
        return (self.completed_story_points / self.total_story_points) * 100.0


@dataclass
class Sprint:
    sprint_id: str
    name: str
    goal: str
    duration_days: int = 10
    user_stories: List[UserStory] = field(default_factory=list)
    daily_remaining_points: List[float] = field(default_factory=list)

    @property
    def total_planned_points(self) -> int:
        return sum(s.story_points for s in self.user_stories)

    @property
    def completed_points(self) -> int:
        return sum(s.story_points for s in self.user_stories if s.status == IssueStatus.DONE)

    def calculate_burndown(self) -> List[float]:
        """
        Calculates day-by-day remaining story points across the sprint duration (Day 0 to Day 10).
        """
        remaining = float(self.total_planned_points)
        burndown = [remaining]
        for day in range(1, self.duration_days + 1):
            for story in self.user_stories:
                if story.completed_day == day and story.status == IssueStatus.DONE:
                    remaining -= story.story_points
            burndown.append(max(0.0, remaining))
        self.daily_remaining_points = burndown
        return burndown


class JiraScrumProject:
    """
    Simulates a Jira Software Scrum Project for Plate Pilot.
    """

    def __init__(self, key: str = "PP", name: str = "Plate Pilot"):
        self.key = key
        self.name = name
        self.epics: Dict[str, Epic] = {}
        self.backlog: List[UserStory] = []
        self.sprints: Dict[str, Sprint] = {}
        self._initialize_backlog()

    def _initialize_backlog(self):
        # 1. Epics
        epic1 = Epic(
            epic_id="PP-EPIC-1",
            title="Personalized Dietary & Meal Planning Engine",
            description="Core computational engine generating 7-day medical meal schedules adhering to calorie limits and allergen rules."
        )
        epic2 = Epic(
            epic_id="PP-EPIC-2",
            title="Nutritional Adherence & Dynamic Adaptation",
            description="Adaptive feedback mechanisms recalculating nutritional targets based on weight trends and adherence logs."
        )
        epic3 = Epic(
            epic_id="PP-EPIC-3",
            title="Order Scheduling, Logistics & Kitchen Dispatch",
            description="Subscriber schedule management, delivery pause/skip controls, and 12-hour kitchen lockouts."
        )
        epic4 = Epic(
            epic_id="PP-EPIC-4",
            title="Health Data Privacy, Security & Compliance",
            description="Role-based clinical isolation, HIPAA-compliant encryption at rest, and dietitian review gatekeeping."
        )

        self.epics = {
            epic1.epic_id: epic1,
            epic2.epic_id: epic2,
            epic3.epic_id: epic3,
            epic4.epic_id: epic4,
        }

        # 2. User Stories (Fibonacci Story Points: 1, 2, 3, 5, 8)
        stories = [
            # Epic 1 Stories
            UserStory(
                story_id="PP-101",
                epic_id="PP-EPIC-1",
                title="Allergen Exclusion Filtering",
                as_a="Subscriber with severe food allergies",
                i_want="the system to strictly filter out recipes containing my excluded allergens",
                so_that="I can consume prepared meals without risking an anaphylactic or allergic reaction",
                story_points=5,
                priority=Priority.HIGH,
                acceptance_criteria=[
                    "Given a subscriber allergy profile (e.g. Peanuts), generated menus contain 0% prohibited ingredients.",
                    "If a recipe has trace allergens, it is automatically flagged and rejected."
                ]
            ),
            UserStory(
                story_id="PP-102",
                epic_id="PP-EPIC-1",
                title="Macronutrient Target Calculator",
                as_a="Subscriber with specific macro goals",
                i_want="my daily calorie, protein, carb, and fat ranges computed from my biometric profile",
                so_that="my meals align precisely with my chronic health and fitness goals",
                story_points=3,
                priority=Priority.HIGH,
                acceptance_criteria=[
                    "Target calories computed within +/- 50 kcal of metabolic requirements.",
                    "Macro ratios sum up to 100% of target caloric intake."
                ]
            ),
            UserStory(
                story_id="PP-103",
                epic_id="PP-EPIC-1",
                title="7-Day Meal Plan Compiler",
                as_a="Subscriber",
                i_want="a complete weekly breakfast, lunch, and dinner schedule generated automatically",
                so_that="I do not have to manually plan or cook individual daily meals",
                story_points=5,
                priority=Priority.HIGH,
                acceptance_criteria=[
                    "Generates 21 distinct meals for a 7-day cycle.",
                    "All 7 days meet daily average caloric targets within a 5% margin."
                ]
            ),

            # Epic 2 Stories
            UserStory(
                story_id="PP-201",
                epic_id="PP-EPIC-2",
                title="Weekly Weight & Adherence Log Entry",
                as_a="Subscriber",
                i_want="to log my end-of-week weight and meal adherence percentage",
                so_that="my dietitian and the algorithm have accurate historical progress data",
                story_points=3,
                priority=Priority.MEDIUM,
                acceptance_criteria=[
                    "Accepts numerical weight (kg) and adherence score (0-100%).",
                    "Validates biometric values against reasonable physiological boundaries."
                ]
            ),
            UserStory(
                story_id="PP-202",
                epic_id="PP-EPIC-2",
                title="Adaptive Macro Recalibration",
                as_a="System Algorithm",
                i_want="to recalculate next week's macro targets based on logged weight deltas",
                so_that="subscribers consistently progress towards their health goals without plateaus",
                story_points=5,
                priority=Priority.HIGH,
                acceptance_criteria=[
                    "Caloric deficit increased by 100 kcal if weight trend is stagnant and adherence is > 85%.",
                    "Recalibration completed automatically prior to Sunday weekly plan generation."
                ]
            ),
            UserStory(
                story_id="PP-203",
                epic_id="PP-EPIC-2",
                title="Dynamic Ingredient Substitution",
                as_a="Kitchen Operator",
                i_want="the system to suggest safe ingredient substitutes when inventory items are out of stock",
                so_that="kitchen fulfillment can proceed without violating allergen or macro constraints",
                story_points=3,
                priority=Priority.LOW,
                acceptance_criteria=[
                    "Substitute maintains allergen safety for the target subscriber.",
                    "Nutrient variation between original and substitute ingredient is under 10%."
                ]
            ),

            # Epic 3 Stories
            UserStory(
                story_id="PP-301",
                epic_id="PP-EPIC-3",
                title="Schedule Modification & Delivery Skip",
                as_a="Subscriber",
                i_want="to pause or skip upcoming meal deliveries from my mobile app",
                so_that="I am not billed or delivered food when traveling or dining out",
                story_points=3,
                priority=Priority.MEDIUM,
                acceptance_criteria=[
                    "UI processes modification request in under 5 seconds (NFR-001).",
                    "Delivery status updates immediately in kitchen dispatch queue."
                ]
            ),
            UserStory(
                story_id="PP-302",
                epic_id="PP-EPIC-3",
                title="12-Hour Kitchen Dispatch Lockout",
                as_a="Kitchen Dispatch Manager",
                i_want="meal modifications locked 12 hours prior to scheduled delivery",
                so_that="kitchen prep and fresh ingredient staging are not disrupted by last-minute changes",
                story_points=5,
                priority=Priority.HIGH,
                acceptance_criteria=[
                    "Modifications within 12 hours of delivery window are rejected with clear error.",
                    "Modifications outside 12 hours are accepted and remaining week macros adjusted."
                ]
            ),

            # Epic 4 Stories
            UserStory(
                story_id="PP-401",
                epic_id="PP-EPIC-4",
                title="Patient Metabolic Data Encryption at Rest",
                as_a="Compliance Officer",
                i_want="all patient metabolic profiles, allergies, and biometrics encrypted at rest using AES-256",
                so_that="the platform complies with HIPAA and prevents sensitive health data exfiltration",
                story_points=5,
                priority=Priority.HIGH,
                acceptance_criteria=[
                    "Raw database inspection reveals zero plain-text allergy or biometric strings.",
                    "Key management enforces separate encryption keys per tenant partition."
                ]
            ),
            UserStory(
                story_id="PP-402",
                epic_id="PP-EPIC-4",
                title="Dietitian-Subscriber RBAC Barrier",
                as_a="Dietitian",
                i_want="access restricted strictly to subscribers explicitly assigned to my clinical caseload",
                so_that="patient confidentiality is strictly maintained between different care providers",
                story_points=5,
                priority=Priority.HIGH,
                acceptance_criteria=[
                    "Unassigned dietitian queries receive HTTP 403 Forbidden.",
                    "Audit log records every clinical profile access event."
                ]
            ),
        ]

        self.backlog = stories
        for story in stories:
            self.epics[story.epic_id].user_stories.append(story)

    def simulate_sprints(self):
        """
        Simulates execution of Sprint 1 and Sprint 2 per Agile-Scrum methodology.
        """
        # SPRINT 1: Core Foundation & Security Framework (18 Story Points)
        sprint1 = Sprint(
            sprint_id="PP-SPRINT-1",
            name="Sprint 1: Core Foundation & Clinical Security",
            goal="Establish core allergen filtering, calorie computation, 7-day meal compiler, and encryption/RBAC security.",
            duration_days=10
        )
        s1_story_ids = ["PP-101", "PP-102", "PP-401", "PP-402", "PP-103"]
        sprint1.user_stories = [s for s in self.backlog if s.story_id in s1_story_ids]

        # Simulate progressive completion across Day 1 to Day 10
        # Day 2: PP-102 (3 pts) completes
        # Day 4: PP-101 (5 pts) completes
        # Day 6: PP-401 (5 pts) completes
        # Day 8: PP-402 (5 pts) completes (cumulative 18 / 18 pts) - Note: PP-103 completes Day 10
        # Let's align cleanly:
        # PP-102 (3) -> Day 2
        # PP-101 (5) -> Day 4
        # PP-401 (5) -> Day 7
        # PP-103 (5) -> Day 10
        # Total S1 = 3 + 5 + 5 + 5 = 18 pts
        # (PP-402 assigned to S2 or S1 - total 18 pts is PP-101 (5), PP-102 (3), PP-103 (5), PP-401 (5) = 18 pts)
        sprint1.user_stories = [
            self.get_story("PP-101"),
            self.get_story("PP-102"),
            self.get_story("PP-103"),
            self.get_story("PP-401"),
        ]
        self.get_story("PP-102").move_to(IssueStatus.DONE, day=2)
        self.get_story("PP-101").move_to(IssueStatus.DONE, day=4)
        self.get_story("PP-401").move_to(IssueStatus.DONE, day=7)
        self.get_story("PP-103").move_to(IssueStatus.DONE, day=10)
        sprint1.calculate_burndown()
        self.sprints["Sprint 1"] = sprint1

        # SPRINT 2: Adaptation, Logistics & RBAC (16 Story Points)
        sprint2 = Sprint(
            sprint_id="PP-SPRINT-2",
            name="Sprint 2: Adaptation, Logistics & Clinical Access",
            goal="Implement adaptive weight recalibration, delivery cutoff controls, RBAC gatekeeper, and substitution.",
            duration_days=10
        )
        sprint2.user_stories = [
            self.get_story("PP-201"),  # 3 pts
            self.get_story("PP-202"),  # 5 pts
            self.get_story("PP-301"),  # 3 pts
            self.get_story("PP-402"),  # 5 pts
        ]
        # Completion progression:
        # Day 2: PP-201 (3 pts) completes
        # Day 5: PP-301 (3 pts) completes
        # Day 7: PP-402 (5 pts) completes
        # Day 9: PP-202 (5 pts) completes
        self.get_story("PP-201").move_to(IssueStatus.DONE, day=2)
        self.get_story("PP-301").move_to(IssueStatus.DONE, day=5)
        self.get_story("PP-402").move_to(IssueStatus.DONE, day=7)
        self.get_story("PP-202").move_to(IssueStatus.DONE, day=9)
        sprint2.calculate_burndown()
        self.sprints["Sprint 2"] = sprint2

    def get_story(self, story_id: str) -> UserStory:
        for s in self.backlog:
            if s.story_id == story_id:
                return s
        raise KeyError(f"Story {story_id} not found in backlog")


if __name__ == "__main__":
    project = JiraScrumProject()
    project.simulate_sprints()
    print(f"Jira Project: {project.name} ({project.key})")
    print(f"Total Epics: {len(project.epics)}")
    print(f"Total Backlog Stories: {len(project.backlog)}")
    for name, sprint in project.sprints.items():
        print(f"\n--- {sprint.name} ---")
        print(f"Planned Points: {sprint.total_planned_points} | Completed: {sprint.completed_points}")
        print(f"Burndown Timeline: {sprint.daily_remaining_points}")
