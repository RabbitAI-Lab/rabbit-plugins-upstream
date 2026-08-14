## Description:

Analyzes GitHub pull requests for mergeability, estimating merge probability and providing conflict and CI status guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill to assess GitHub pull requests before merge by reviewing mergeability signals, conflict risk, CI status, and recommended follow-up actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for write and command execution authority while the stated purpose is GitHub pull request mergeability analysis.

Mitigation: Review before installing, run only in a constrained environment, and do not grant write or command execution authority unless the publisher narrows scope and documents exact commands.

Risk: Private repository analysis can require credentials or repository access that may expose sensitive source information.

Mitigation: Use least-privilege repository access, pass credentials only through approved environment handling, and review publisher guidance for private repository credential handling before use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/merge-check)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown report with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include merge probability, conflict warnings, CI status, and recommendations.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
