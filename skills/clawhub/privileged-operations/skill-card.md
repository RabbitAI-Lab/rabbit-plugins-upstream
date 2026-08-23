## Description:

Guides agents through Linux tasks that may require root privileges by keeping work unprivileged until a narrow, visible, user-approved elevation is necessary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[pinguy](https://clawhub.ai/user/pinguy)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and agents use this skill when planning or executing Linux tasks that might cross the root privilege boundary. It helps keep inspection, builds, validation, and diagnosis unprivileged while making any necessary privileged action explicit and user-controlled.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A proposed root command could change protected system state.

Mitigation: Review the exact command, reason, target path, device, or service before approving visible interactive authentication.

Risk: Hidden or automated credential handling would weaken the user approval boundary.

Mitigation: Use pkexec, sudo, or doas only when the prompt is visible to the user, and never share, capture, pipe, cache, or automate passwords.

Risk: Broad privileged shells or command chains can expand authority beyond the intended action.

Mitigation: Keep inspection, downloads, builds, and validation unprivileged, then elevate only one narrow verified operation at a time.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/pinguy/Skills/tree/main/skills/privileged-operations)
- [ClawHub skill page](https://clawhub.ai/pinguy/skills/privileged-operations)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell-command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Proposes bounded privileged actions and verification steps; does not handle user passwords.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
