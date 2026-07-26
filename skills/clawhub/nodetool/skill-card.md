## Description: <br>
Visual AI workflow builder - ComfyUI meets n8n for LLM agents, RAG pipelines, and multimodal data flows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[georgi](https://clawhub.ai/user/georgi) <br>

### License/Terms of Use: <br>
AGPL-3.0 <br>


## Use Case: <br>
Developers and engineers use this skill to install and operate Nodetool for local AI workflow building, including LLM agents, RAG pipelines, multimodal flows, workflow execution, model management, and deployment tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Remote installer commands can execute upstream scripts directly, including silent installation modes that skip prompts. <br>
Mitigation: Download and review installers before execution, prefer pinned releases or checksums when available, and use silent installation only in controlled environments. <br>
Risk: Workflow commands may accept auth tokens or show settings, which can expose secrets through shell history, logs, or terminal output. <br>
Mitigation: Avoid placing real tokens in command history or logs, use environment-specific secret handling, and confirm before displaying settings or secrets. <br>
Risk: Server, proxy, sync, and cloud deployment commands can expose local services or modify remote infrastructure. <br>
Mitigation: Confirm host bindings, proxy daemon behavior, data synchronization targets, and deployment apply/destroy actions before running them. <br>


## Reference(s): <br>
- [Nodetool ClawHub Skill Page](https://clawhub.ai/georgi/skills/nodetool) <br>
- [Nodetool Website](https://nodetool.ai) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSONL-oriented workflow execution examples for automation.] <br>

## Skill Version(s): <br>
0.6.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
