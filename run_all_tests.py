"""
Master Test Runner for SE Lab Submissions (Labs 1 through 7)
Course: Software Engineering (UE24CS351A)
Student: Roshan (PES1UG24CS387)
"""

import sys
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent

LABS = [
    {
        "name": "Lab 1: Requirements Engineering & UML Use-Case Modelling",
        "dir": ROOT / "Lab 1",
        "cmd": [sys.executable, "-m", "pytest", "test_plate_pilot.py", "-q"],
    },
    {
        "name": "Lab 2: Agile Backlog Creation & Sprint Simulation in Jira",
        "dir": ROOT / "Lab 2",
        "cmd": [sys.executable, "-m", "pytest", "test_agile_simulation.py", "-q"],
    },
    {
        "name": "Lab 3: Architecture & Component Modelling",
        "dir": ROOT / "Lab 3",
        "cmd": [sys.executable, "-m", "pytest", "test_architecture.py", "-q"],
    },
    {
        "name": "Lab 4: Vibe Coding - Blackjack vs Dealer",
        "dir": ROOT / "Lab 4",
        "cmd": [sys.executable, "-m", "pytest", "test_blackjack.py", "-q"],
    },
    {
        "name": "Lab 5: Static Analysis - Bike Share Stations",
        "dir": ROOT / "Lab 5",
        "cmd": [sys.executable, "-m", "pytest", "test_bike_share_stations.py", "-q"],
    },
    {
        "name": "Lab 6: Line & Branch Coverage - Shopping Cart",
        "dir": ROOT / "Lab 6",
        "cmd": [sys.executable, "-m", "pytest", "test_shopping_cart.py", "-q"],
    },
    {
        "name": "Lab 7: Fuzz Testing - Shopping Cart / Hypothesis",
        "dir": ROOT / "Lab 7",
        "cmd": [sys.executable, "-m", "pytest", "test_processor.py", "-q"],
    },
]


def main():
    print("=" * 75)
    print("       SOFTWARE ENGINEERING LAB SUBMISSIONS MASTER TEST RUNNER")
    print("       Student SRN: PES1UG24CS387 | GitHub: Roshan2607/plate-pilot")
    print("=" * 75)

    results = []
    all_passed = True

    for lab in LABS:
        print(f"\n[RUNNING] {lab['name']}...")
        proc = subprocess.run(lab["cmd"], cwd=lab["dir"], capture_output=True, text=True)
        passed = (proc.returncode == 0)
        status_text = "PASSED" if passed else "FAILED"
        results.append((lab["name"], status_text, proc.stdout.strip()))

        if passed:
            summary = proc.stdout.strip().splitlines()[-1] if proc.stdout else "PASSED"
            print(f"  -> [OK] {summary}")
        else:
            all_passed = False
            print(f"  -> [FAIL] {proc.stderr or proc.stdout}")

    print("\n" + "=" * 75)
    print(f"{'Lab':<58} | {'Status':<12}")
    print("-" * 75)
    for name, status, _ in results:
        print(f"{name:<58} | {status:<12}")
    print("=" * 75)

    if all_passed:
        print("\nALL LABS EXECUTED AND PASSED SUCCESSFULLY! (7 / 7)")
        sys.exit(0)
    else:
        print("\nSOME LAB TESTS FAILED. PLEASE INSPECT OUTPUT ABOVE.")
        sys.exit(1)


if __name__ == "__main__":
    main()
