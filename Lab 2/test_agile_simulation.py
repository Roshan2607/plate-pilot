"""
Unit tests for Lab 2: Agile Backlog Creation & Sprint Simulation in Jira
Software Engineering (UE24CS351A) - PES1UG24CS387
Validates exact PLAT Jira Board deliverables (https://plate-pilot.atlassian.net).
"""

import pytest
from agile_simulation import JiraScrumProject, IssueStatus, Priority


@pytest.fixture
def project():
    return JiraScrumProject()


def test_epics_initialization(project):
    """Verify that all 4 Epics from the PLAT board are present."""
    expected_epics = [
        "Customer Ordering Experience",
        "Epic 2: Meal Plan Generation & Customization",
        "Epic 3: Subscription & Delivery Management",
        "Epic 4: Health Tracking & Adaptive Targets"
    ]
    assert len(project.epics) == 4
    for epic_name in expected_epics:
        assert epic_name in project.epics
        assert project.epics[epic_name].total_story_points > 0


def test_fibonacci_story_points(project):
    """Verify all 7 stories follow strict Fibonacci values [1, 2, 3, 5, 8, 13, 21]."""
    fibonacci_set = {1, 2, 3, 5, 8, 13, 21}
    assert len(project.backlog) == 7
    total_points = 0
    for story in project.backlog:
        assert story.story_points in fibonacci_set
        assert story.story_id.startswith("PLAT-")
        assert len(story.title) > 0
        total_points += story.story_points
    # Total backlog points must equal exactly 53
    assert total_points == 53
    assert project.total_backlog_points == 53


def test_active_sprint_board_status(project):
    """Verify the exact distribution across To Do, In Progress, and Done on PLAT board."""
    done_items = [s for s in project.backlog if s.status == IssueStatus.DONE]
    in_progress_items = [s for s in project.backlog if s.status == IssueStatus.IN_PROGRESS]
    to_do_items = [s for s in project.backlog if s.status == IssueStatus.TO_DO]

    # Done: PLAT-5 (1 SP), PLAT-6 (2 SP)
    assert len(done_items) == 2
    assert {s.story_id for s in done_items} == {"PLAT-5", "PLAT-6"}
    assert sum(s.story_points for s in done_items) == 3

    # In Progress: PLAT-7 (3 SP), PLAT-8 (5 SP)
    assert len(in_progress_items) == 2
    assert {s.story_id for s in in_progress_items} == {"PLAT-7", "PLAT-8"}
    assert sum(s.story_points for s in in_progress_items) == 8

    # To Do: PLAT-9 (8 SP), PLAT-10 (13 SP), PLAT-11 (21 SP)
    assert len(to_do_items) == 3
    assert {s.story_id for s in to_do_items} == {"PLAT-9", "PLAT-10", "PLAT-11"}
    assert sum(s.story_points for s in to_do_items) == 42


def test_epic_progress_tracking(project):
    """Verify Epic completion metrics from active sprint."""
    epic1 = project.epics["Customer Ordering Experience"]
    # PLAT-5 is 1 SP and DONE
    assert epic1.total_story_points == 1
    assert epic1.completed_story_points == 1
    assert epic1.progress_percentage == 100.0

    epic2 = project.epics["Epic 2: Meal Plan Generation & Customization"]
    # Total 2 + 3 + 5 = 10 SP, completed PLAT-6 = 2 SP
    assert epic2.total_story_points == 10
    assert epic2.completed_story_points == 2
    assert epic2.progress_percentage == 20.0


def test_jira_workspace_references(project):
    """Verify Atlassian workspace keys and URLs match submission."""
    assert project.key == "PLAT"
    assert "plate-pilot.atlassian.net" in project.jira_url
    assert project.share_url == "https://tinyurl.com/37cz6put"
