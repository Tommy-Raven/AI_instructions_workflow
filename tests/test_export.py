"""
Tests export functionality for Graphviz and multi-mode output.
"""

from ai_visualization.export_manager import export_workflow
import os


def test_export_workflow_json_and_md(tmp_path):
    wf = {
        "workflow_id": "test_workflow",
        "version": "1.0",
        "metadata": {"purpose": "Export test"},
        "phases": [{"title": "Phase 1", "tasks": ["Run", "Save"]}],
        "dependency_graph": {"nodes": ["Run", "Save"], "edges": [["Run", "Save"]]},
    }

    exports = export_workflow(wf, export_mode="both")
    for key, path in exports.items():
        assert os.path.exists(path), f"{key} export failed: {path}"
