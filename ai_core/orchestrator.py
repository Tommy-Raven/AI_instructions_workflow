from generator.main import generate_workflow
from ai_memory.memory_store import MemoryStore
from ai_validation.schema_validator import validate_workflow
from utils import log

class Orchestrator:
    def __init__(self):
        self.memory = MemoryStore()

    def run(self, user_config):
        log("Starting workflow orchestration…")
        wf = generate_workflow(user_config)

        valid, err = validate_workflow(wf)
        if not valid:
            log(f"Schema validation failed: {err}", level="ERROR")
            raise ValueError(f"Invalid workflow schema: {err}")

        self.memory.save(wf)
        log(f"Workflow {wf.get('workflow_id', '<no-id>')} stored in memory.")
        return wf
