"""
Generates publication-quality Jira Sprint Burndown Charts for Lab 2
Software Engineering (UE24CS351A) - PES1UG24CS387
"""

import matplotlib.pyplot as plt
import numpy as np
from agile_simulation import JiraScrumProject

def generate_charts():
    project = JiraScrumProject()
    project.simulate_sprints()

    plt.style.use('seaborn-v0_8-whitegrid' if 'seaborn-v0_8-whitegrid' in plt.style.available else 'default')

    for sprint_name, sprint in project.sprints.items():
        days = list(range(sprint.duration_days + 1))
        initial_points = sprint.total_planned_points
        ideal_guideline = [initial_points - (initial_points / sprint.duration_days) * d for d in days]
        actual_remaining = sprint.daily_remaining_points

        fig, ax = plt.subplots(figsize=(9, 5.5), dpi=300)

        # Plot Guideline (Grey dashed line)
        ax.plot(days, ideal_guideline, color='#888888', linestyle='--', linewidth=2.2, label='Guideline (Ideal Burn)')

        # Plot Remaining Effort (Red/Crimson line per Jira standard)
        ax.step(days, actual_remaining, where='post', color='#D9381E', linewidth=2.8, label='Remaining Values (Actual)')
        ax.plot(days, actual_remaining, 'o', color='#D9381E', markersize=6)

        # Fill under curve
        ax.fill_between(days, actual_remaining, step='post', alpha=0.12, color='#D9381E')

        # Formatting
        ax.set_title(f"Jira Software Burndown Chart: {sprint.name}\nProject: Plate Pilot (PP) | Student: PES1UG24CS387", fontsize=13, fontweight='bold', pad=15)
        ax.set_xlabel("Sprint Timeline (Days)", fontsize=11, fontweight='semibold')
        ax.set_ylabel("Story Points (Remaining)", fontsize=11, fontweight='semibold')
        ax.set_xticks(days)
        ax.set_xticklabels([f"Day {d}" if d > 0 else "Start (D0)" for d in days], rotation=30)
        ax.set_ylim(-0.5, initial_points + 2)
        ax.grid(True, linestyle=':', alpha=0.6)
        ax.legend(frameon=True, loc='upper right', fontsize=10)

        # Annotations for completions
        for s in sprint.user_stories:
            if s.completed_day:
                ax.annotate(
                    f"{s.story_id} Done (-{s.story_points} SP)",
                    xy=(s.completed_day, actual_remaining[s.completed_day]),
                    xytext=(s.completed_day - 0.5, actual_remaining[s.completed_day] + 1.2),
                    arrowprops=dict(facecolor='#2E7D32', shrink=0.08, width=1, headwidth=5),
                    fontsize=8.5,
                    fontweight='bold',
                    color='#1B5E20'
                )

        fig.tight_layout()
        out_filename = "burndown_chart_sprint1.png" if "Sprint 1" in sprint_name else "burndown_chart_sprint2.png"
        fig.savefig(out_filename, dpi=300)
        plt.close(fig)
        print(f"Generated chart: {out_filename}")

if __name__ == "__main__":
    generate_charts()
