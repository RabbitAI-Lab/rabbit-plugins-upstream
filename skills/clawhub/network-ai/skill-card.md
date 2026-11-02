## Description:

Local Python orchestration skill: multi-agent workflows via shared blackboard file, permission gating, token budget scripts, and persistent project context. The bundled Python scripts make no network calls and have zero third-party dependencies. The parent repository also contains a TypeScript engine (not included in this skill bundle).

This skill is ready for commercial/non-commercial use.

## Publisher:

[jovancoding](https://clawhub.ai/user/jovancoding)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use the bundled Python tools to coordinate work in a trusted local workspace, track tasks and budgets, manage advisory permission grants, and maintain project context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Manipulated local file links may redirect state-file writes outside the project boundary and damage other files.

Mitigation: Use an isolated, user-owned workspace, prevent untrusted changes to data/, and require symlink-safe handling for lock, archive, and other state files before relying on the project boundary.

Risk: Free-text justifications and project notes may persist sensitive information, and advisory tokens may be mistaken for authenticated authorization.

Mitigation: Keep secrets and personal information out of logs and project notes, and do not use advisory tokens as real authorization.

## Reference(s):

- [Network-AI homepage](https://network-ai.org)
- [Network-AI ClawHub release](https://clawhub.ai/jovancoding/skills/network-ai)

## Skill Output:

**Output Type(s):** [Files, JSON, Markdown, Text]

**Output Format:** [Local Markdown and JSON state files, with text or JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State is stored locally; scripts run only when explicitly invoked.]

## Skill Version(s):

5.17.2 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
