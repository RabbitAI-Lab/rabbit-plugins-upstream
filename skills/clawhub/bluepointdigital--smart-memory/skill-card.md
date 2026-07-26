## Description: <br>
Persistent local transcript-first memory for OpenClaw via a Node adapter and FastAPI engine. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bluepointdigital](https://clawhub.ai/user/bluepointdigital) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use Smart Memory to give OpenClaw-style local agents durable recall, transcript-backed memory commits, revision-aware retrieval, prompt context composition, and inspection of memory evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill persistently stores conversation history on disk. <br>
Mitigation: Use it only for data you are comfortable storing locally, avoid secrets or regulated data, and add retention and deletion controls before sensitive use. <br>
Risk: Setup and runtime behavior can download and execute dependencies and run a local service. <br>
Mitigation: Review the installer and dependency setup, pin the source before use, and restrict the service to localhost. <br>
Risk: Background or auto-start behavior may run when not expected. <br>
Mitigation: Disable or gate auto-start and background behavior unless it is needed for the deployment. <br>


## Reference(s): <br>
- [Smart Memory ClawHub listing](https://clawhub.ai/bluepointdigital/skills/smart-memory) <br>
- [README](artifact/README.md) <br>
- [Integration Guide](artifact/INTEGRATION.md) <br>
- [Memory Structure](artifact/MEMORY_STRUCTURE.md) <br>
- [OpenClaw Skill README](artifact/skills/smart-memory-openclaw/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and text tool responses with shell command and JSON examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local memory responses may include retrieved memories, commit status, pending insights, and evidence or inspection details.] <br>

## Skill Version(s): <br>
3.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
