## Description: <br>
stellar-trails provides an always-on, six-phase workflow controller for agent tasks with traceability gates, scope commitment, and adaptive task complexity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hoshiyomix](https://clawhub.ai/user/hoshiyomix) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to structure coding, document, data-processing, visualization, planning, and troubleshooting work through explicit phases, gates, and delivery checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill runs as an always-on workflow controller with local process management and persistent state. <br>
Mitigation: Install only when that behavior is intended, review the activation workflow before use, and monitor or prune persistent logs and state. <br>
Risk: The skill starts a local popup server that may be network-visible depending on the environment. <br>
Mitigation: Bind the server to localhost or disable the popup server before deployment in shared or exposed environments. <br>
Risk: The skill includes automatic self-update and process-kill behavior. <br>
Mitigation: Review or remove automatic update and process termination steps before use in controlled environments. <br>
Risk: The skill can handle GitHub personal access tokens and may store credentials in ~/.git-credentials. <br>
Mitigation: Provide a GitHub token only when required, avoid persistent credential storage unless explicitly approved, and use least-privilege tokens. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/hoshiyomix/skills/stellar-trails) <br>
- [Workflow Phases](procedure/phases.md) <br>
- [Error Resolution Decision Tree](procedure/error-resolution.md) <br>
- [AskUserQuestion Gate Template](references/askuserquestion-gate.md) <br>
- [SADC Subagent Delegation Template](references/sadc-subagent-delegation.md) <br>
- [z.ai Sandbox Constraints](knowledge/zai-sandbox.md) <br>
- [Code Standards](constraints/code-standards.md) <br>
- [Type Safety](constraints/type-safety.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and plain text with checklists, status markers, code snippets, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include phase markers, traceability IDs, verification reports, local server commands, and configuration guidance.] <br>

## Skill Version(s): <br>
9.10.0 (source: SKILL.md metadata and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
