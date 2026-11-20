"""
Lab 2: Agile Backlog Creation & Sprint Simulation in Jira
Software Engineering (UE24CS351A)
Student SRN: PES1UG24CS387
Domain: Plate Pilot (Healthcare & Telemedicine Dietary Management System)
Jira Workspace: https://plate-pilot.atlassian.net (PLAT board)
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
    epic_title: str
    title: str
    as_a: str
    i_want: str
    so_that: str
    story_points: int
    priority: Priority
    status: IssueStatus = IssueStatus.TO_DO
    completed_day: Optional[int] = None

    def move_to(self, new_status: IssueStatus, day: Optional[int] = None):
        self.status = new_status
        if new_status == IssueStatus.DONE:
            self.completed_day = day


@dataclass
class Epic:
    title: str
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
    name: str
    duration_days: int = 7
    user_stories: List[UserStory] = field(default_factory=list)
    daily_remaining_points: List[float] = field(default_factory=list)

    @property
    def total_planned_points(self) -> int:
        return sum(s.story_points for s in self.user_stories)

    @property
    def completed_points(self) -> int:
        return sum(s.story_points for s in self.user_stories if s.status == IssueStatus.DONE)


class JiraScrumProject:
    """
    Exact simulation of Roshan's Jira Software Scrum Project for Plate Pilot (PLAT Board).
    Atlassian Cloud Site: https://plate-pilot.atlassian.net
    """

    def __init__(self, key: str = "PLAT", name: str = "Plate Pilot"):
        self.key = key
        self.name = name
        self.jira_url = "https://plate-pilot.atlassian.net"
        self.share_url = "https://tinyurl.com/37cz6put"
        self.epics: Dict[str, Epic] = {}
        self.backlog: List[UserStory] = []
        self._initialize_backlog()

    def _initialize_backlog(self):
        # 1. Epics per PLAT board
        epic_names = [
            "Customer Ordering Experience",
            "Epic 2: Meal Plan Generation & Customization",
            "Epic 3: Subscription & Delivery Management",
            "Epic 4: Health Tracking & Adaptive Targets"
        ]
        self.epics = {name: Epic(title=name) for name in epic_names}

        # 2. Exact 7 User Stories from student Jira PLAT board (Fibonacci sequence: 1, 2, 3, 5, 8, 13, 21 = 53 SP)
        stories = [
            UserStory(
                story_id="PLAT-5",
                epic_title="Customer Ordering Experience",
                title="User Authentication",
                as_a="Subscriber / Dietitian",
                i_want="to securely sign in to my Plate Pilot account",
                so_that="I can view and manage my personalized dietary meal plans securely",
                story_points=1,
                priority=Priority.LOW,
                status=IssueStatus.DONE,
                completed_day=1
            ),
            UserStory(
                story_id="PLAT-6",
                epic_title="Epic 2: Meal Plan Generation & Customization",
                title="Automated Weekly Meal Plan Generation",
                as_a="Subscriber with dietary constraints",
                i_want="the system to automatically generate weekly meal plans adhering to my macros and allergen exclusions",
                so_that="I receive nutritionally balanced, medically safe meals without manual planning",
                story_points=2,
                priority=Priority.HIGH,
                status=IssueStatus.DONE,
                completed_day=2
            ),
            UserStory(
                story_id="PLAT-7",
                epic_title="Epic 2: Meal Plan Generation & Customization",
                title="Dietitian Review and Edit Plan",
                as_a="Assigned Dietitian",
                i_want="to review, adjust, or override auto-generated patient meal plans before dispatch",
                so_that="I ensure medical soundness and clinical efficacy for each subscriber",
                story_points=3,
                priority=Priority.MEDIUM,
                status=IssueStatus.IN_PROGRESS
            ),
            UserStory(
                story_id="PLAT-8",
                epic_title="Epic 2: Meal Plan Generation & Customization",
                title="Ingredient Substitution Proposals",
                as_a="Kitchen Operator",
                i_want="the system to propose safe ingredient substitutes when items are out of stock",
                so_that="meal preparation continues without violating allergen or macronutrient rules",
                story_points=5,
                priority=Priority.LOW,
                status=IssueStatus.IN_PROGRESS
            ),
            UserStory(
                story_id="PLAT-9",
                epic_title="Epic 3: Subscription & Delivery Management",
                title="Manage Deliveries (Pause, Skip, Reschedule)",
                as_a="Subscriber",
                i_want="to pause, skip, or reschedule upcoming deliveries up to 12 hours before dispatch",
                so_that="I have flexibility during travel while maintaining my nutritional plan",
                story_points=8,
                priority=Priority.MEDIUM,
                status=IssueStatus.TO_DO
            ),
            UserStory(
                story_id="PLAT-10",
                epic_title="Epic 4: Health Tracking & Adaptive Targets",
                title="Log Adherence and Weight",
                as_a="Subscriber",
                i_want="to log weekly biometric weight and meal consumption adherence",
                so_that="my historical progress is tracked and shared with my clinical dietitian",
                story_points=13,
                priority=Priority.LOW,
                status=IssueStatus.TO_DO
            ),
            UserStory(
                story_id="PLAT-11",
                epic_title="Epic 4: Health Tracking & Adaptive Targets",
                title="Recalculate Macro Targets",
                as_a="Adaptive Diet Engine",
                i_want="to automatically recalculate next week's calorie and macro targets from logged adherence",
                so_that="the subscriber's diet plan adapts dynamically to avoid metabolic plateaus",
                story_points=21,
                priority=Priority.LOW,
                status=IssueStatus.TO_DO
            ),
        ]

        self.backlog = stories
        for story in stories:
            self.epics[story.epic_title].user_stories.append(story)

    def get_story(self, story_id: str) -> UserStory:
        for s in self.backlog:
            if s.story_id == story_id:
                return s
        raise KeyError(f"Story {story_id} not found in backlog")

    @property
    def total_backlog_points(self) -> int:
        return sum(s.story_points for s in self.backlog)


if __name__ == "__main__":
    project = JiraScrumProject()
    print(f"Jira Project: {project.name} ({project.key})")
    print(f"URL: {project.jira_url} (Invite: {project.share_url})")
    print(f"Total Epics: {len(project.epics)}")
    print(f"Total Backlog Stories: {len(project.backlog)}")
    print(f"Total Story Points: {project.total_backlog_points} SP")
    print("\n--- SPRINT BOARD STATUS ---")
    for status in [IssueStatus.TO_DO, IssueStatus.IN_PROGRESS, IssueStatus.DONE]:
        items = [s for s in project.backlog if s.status == status]
        pts = sum(s.story_points for s in items)
        print(f"{status.value} ({len(items)} items - {pts} SP): {', '.join(s.story_id for s in items)}")
