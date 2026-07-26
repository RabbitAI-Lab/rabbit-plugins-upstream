## Description: <br>
Cloud memory for AI agents. Writes are free, pay only for reads. First 25 calls free, 7-day persistence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[natmota](https://clawhub.ai/user/natmota) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use AgentMem to store and retrieve agent memories through AgentMem's hosted API for session persistence, cross-device sync, team knowledge, and long-term learning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Agent memories may be persisted to AgentMem's third-party cloud service, including sensitive or regulated content if agents store raw context. <br>
Mitigation: Use synthetic data for demos and avoid storing secrets, credentials, private user details, regulated data, or raw conversation context. <br>
Risk: Public memory sharing can expose stored content when public=true or public feed workflows are used. <br>
Mitigation: Disable public=true unless there is explicit approval, and review memory content before publishing or sharing. <br>
Risk: Scheduled or automatic memory sync can transfer more context than intended and complicate retention or deletion expectations. <br>
Mitigation: Limit stored values to minimal summaries, keep scheduled sync disabled until approved, and define retention and deletion expectations before use. <br>


## Reference(s): <br>
- [ClawHub AgentMem listing](https://clawhub.ai/natmota/skills/agentmem) <br>
- [AgentMem website](https://agentmem.io) <br>
- [AgentMem API base URL](https://api.agentmem.io/v1) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown instructions with curl command examples and API workflow guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guidance can cause agents to send memory content to AgentMem's hosted API for storage, retrieval, deletion, listing, and optional public sharing.] <br>

## Skill Version(s): <br>
2.4.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
