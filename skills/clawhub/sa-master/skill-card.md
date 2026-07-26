## Description: <br>
Sa Master helps agents turn business-analysis assets into architecture design documents, API and interface documentation, deployment guides, and detailed design review reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leo21cn](https://clawhub.ai/user/leo21cn) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, architects, and engineering teams use this skill to convert PRDs, conceptual diagrams, architecture baselines, and detailed design documents into structured architecture deliverables and review feedback. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive architecture documents, requirements, API details, and deployment information may be sent to an external MCP service. <br>
Mitigation: Use only with approved materials and confirm data-handling expectations before connecting the service. <br>
Risk: The package includes an exposed bearer token for the remote MCP service. <br>
Mitigation: Rotate the token, remove secrets from the package, and require user-provided secret configuration. <br>
Risk: The security verdict is suspicious because external data sharing has limited user-facing disclosure. <br>
Mitigation: Review the package before installation and add explicit consent and data-handling notice before routine use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/leo21cn/skills/sa-master) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown documents with Mermaid diagrams, structured review reports, and staged tool responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use a remote MCP service to generate architecture deliverables and exported artifacts.] <br>

## Skill Version(s): <br>
1.8.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
