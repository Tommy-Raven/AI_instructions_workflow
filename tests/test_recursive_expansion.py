"""
Tests workflow regeneration from diff and recursion engine.
"""

from ai_recursive.version_diff_engine import compute_diff_summary


def test_diff_summary_detects_changes():
    wf_old = {"metadata": {"purpose": "Old"}, "phases": [{"title": "A"}]}
    wf_new = {"metadata": {"purpose": "New"}, "phases": [{"title": "A"}, {"title": "B"}]}

    diff = compute_diff_summary(wf_old, wf_new)
    assert diff["diff_size"] >= 2
    assert diff["added_phases"] == ["B"]

