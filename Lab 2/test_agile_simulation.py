"""
Unit tests for Lab 2: Agile Backlog Creation & Sprint Simulation in Jira
Software Engineering (UE24CS351A) - PES1UG24CS387
"""

import pytest
from agile_simulation import JiraScrumProject, IssueStatus, Priority

@pytest.fixture
def project():
    proj = JiraScrumProject()
    proj.simulate_sprints()
    return proj

def test_epics_initialization(project):
    """Verify that all major functional themes from Lab 1 are mapped to Jira Epics."""
    assert len(project.epics) == 4
    expected_epics = ["PP-EPIC-1", "PP-EPIC-2", "PP-EPIC-3", "PP-EPIC-4"]
    for epic_id in expected_epics:
        assert epic_id in project.epics
        assert project.epics[epic_id].total_story_points > 0

def test_fibonacci_story_points(project):
    """Verify all story point estimates strictly follow the Fibonacci sequence."""
    fibonacci_set = {1, 2, 3, 5, 8, 13}
    for story in project.backlog:
        assert story.story_points in fibonacci_set
        assert story.as_a is not None and len(story.as_a) > 0
        assert story.i_want is not None and len(story.i_want) > 0
        assert story.so_that is not None and len(story.so_that) > 0
        assert len(story.acceptance_criteria) >= 1

def test_sprint_1_velocity_and_burndown(project):
    """Verify Sprint 1 simulation: 18 Story Points planned and burned down to 0."""
    sprint1 = project.sprints["Sprint 1"]
    assert sprint1.total_planned_points == 18
    assert sprint1.completed_points == 18
    assert len(sprint1.daily_remaining_points) == 11  # Day 0 to Day 10
    assert sprint1.daily_remaining_points[0] == 18.0
    assert sprint1.daily_remaining_points[-1] == 0.0
    # Check that remaining points are monotonically non-increasing
    for i in range(len(sprint1.daily_remaining_points) - 1):
        assert sprint1.daily_remaining_points[i] >= sprint1.daily_remaining_points[i+1]

def test_sprint_2_velocity_and_burndown(project):
    """Verify Sprint 2 simulation: 16 Story Points planned and burned down to 0."""
    sprint2 = project.sprints["Sprint 2"]
    assert sprint2.total_planned_points == 16
    assert sprint2.completed_points == 16
    assert len(sprint2.daily_remaining_points) == 11
    assert sprint2.daily_remaining_points[0] == 16.0
    assert sprint2.daily_remaining_points[-1] == 0.0
    for i in range(len(sprint2.daily_remaining_points) - 1):
        assert sprint2.daily_remaining_points[i] >= sprint2.daily_remaining_points[i+1]

def test_epic_progress_tracking(project):
    """Verify Epic completion metrics after sprint execution."""
    epic1 = project.epics["PP-EPIC-1"]
    # All 3 stories completed in Sprint 1 (5 + 3 + 5 = 13 pts)
    assert epic1.completed_story_points == 13
    assert epic1.progress_percentage == 100.0

def test_user_story_state_transitions(project):
    """Verify state transitions of stories to DONE."""
    for sprint in project.sprints.values():
        for story in sprint.user_stories:
            assert story.status == IssueStatus.DONE
            assert story.completed_day is not None
            assert 1 <= story.completed_day <= 10
