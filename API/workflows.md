# 🧩 Workflow API

Workflow-related endpoints and functions allow external systems to invoke
the full SSWG–MVM pipeline, including:

- Workflow creation
- Refinement & recursion
- Validation
- Export (JSON, Markdown, Mermaid)

---

## 🛠️ Core Functions (Python API)

### `generate_workflow(input_data: dict) -> dict`
Generate a new workflow from user parameters.

### `refine_workflow(workflow: dict, depth: int = 1) -> dict`
Perform recursive refinement passes using the Recursion Manager.

### `validate_workflow(workflow: dict) -> tuple[bool, str]`
Schema validation against `schemas/workflow_schema.json`.

### `export_json(workflow: dict, out_dir: str) -> str`
Save workflow as JSON.

### `export_markdown(workflow: dict, out_dir: str) -> str`
Save workflow as Markdown for human-readable inspection.

---

## 🌐 REST API Overview

### `POST /api/workflows/generate`
Creates a workflow from user input.

### `POST /api/workflows/refine`
Refines an existing workflow.

### `POST /api/workflows/validate`
Validates a workflow against SSWG schema.

### `GET /api/workflows/export/{id}`
Exports
