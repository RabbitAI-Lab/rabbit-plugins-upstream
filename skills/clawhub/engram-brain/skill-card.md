## Description: <br>
Native local memory for OpenClaw agents: Capture, Cue, Project, Recall, and Consolidate conversations into a private Helix-backed brain. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[moshik21](https://clawhub.ai/user/moshik21) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use Engram Memory to give OpenClaw agents local long-term memory, project context recall, sparse durable fact promotion, and offline memory consolidation across sessions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill stores and reuses durable local conversation and project memory, which may include sensitive data. <br>
Mitigation: Install only when durable local memory is acceptable; review what is captured and know how to stop the service and delete stored memories. <br>
Risk: The setup starts local services, writes OpenClaw MCP configuration, and runs background memory hygiene. <br>
Mitigation: Review configuration changes before relying on the integration and confirm service status with the documented runtime checks. <br>
Risk: The install path uses an unpinned remote shell installer. <br>
Mitigation: Inspect the installer source and trust boundary before running it, or use an existing trusted Engram installation path. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/moshik21/skills/engram-brain) <br>
- [Publisher profile](https://clawhub.ai/user/moshik21) <br>
- [Engram project homepage](https://github.com/Moshik21/engram) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands, REST examples, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides local memory capture, recall, promotion, service setup, MCP configuration, and runtime checks.] <br>

## Skill Version(s): <br>
0.3.5 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
