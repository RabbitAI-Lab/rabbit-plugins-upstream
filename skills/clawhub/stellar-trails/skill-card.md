## Description:

Stellar Trails provides an always-on six-phase workflow framework that guides agents through task classification, planning, execution, validation, and delivery with traceability gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hoshiyomix](https://clawhub.ai/user/hoshiyomix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to impose a structured workflow on coding, document, visualization, data-processing, planning, and general task requests. It is intended to make agent work more traceable through phase gates, activation checks, and delivery records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may start and manage a local preview server on port 3000.

Mitigation: Install it only in workspaces where local preview-server management is expected, and stop or isolate conflicting services before activation.

Risk: The skill may write persistent logs and cross-session work records.

Mitigation: Use it only where workflow logging is acceptable, and review stored logs before sharing or archiving the workspace.

Risk: The skill may self-update and use a GitHub PAT from the documented path.

Mitigation: Do not install it in workspaces where automatic credential setup, global git config changes, or PAT-backed operations are unacceptable.

## Reference(s):

- [AskUserQuestion Gate Template](references/askuserquestion-gate.md)
- [ClawHub skill page](https://clawhub.ai/hoshiyomix/skills/stellar-trails)
- [Publisher profile](https://clawhub.ai/user/hoshiyomix)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and task-state records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May start local workflow support services and write persistent workflow logs as part of activation.]

## Skill Version(s):

9.13.3 (source: server release and artifact metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
