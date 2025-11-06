"""
Tests utility consistency and schema enforcement.
"""

from ai_validation.schema_validator import validate_workflow


def test_schema_validator_rejects_invalid():
    invalid_wf = {"version": "1.0", "metadata": {}}
    valid, err = validate_workflow(invalid_wf)
    assert not valid
    assert "required" in err.lower()
