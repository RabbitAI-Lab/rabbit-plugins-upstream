## Description:

Monitor a Dataify Builder task through completion, recover safely after interruption, or guide cross-platform DATAIFY_API_TOKEN setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to monitor existing Dataify Builder tasks, retrieve final JSON results, recover after interrupted monitoring, and configure the required API token without exposing the token in chat.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports broader bundled Dataify submission and business-intelligence workflows beyond the advertised monitoring purpose.

Mitigation: Review bundled workflows before installation and use only task IDs, target URLs, and parameters from trusted sources.

Risk: The security review reports generated shell-command paths with injection risks.

Mitigation: Avoid copying preview or resume commands generated from untrusted input; prefer validated task IDs and safely quoted commands.

Risk: Dataify tasks can consume credits or process high-volume collections.

Mitigation: Confirm before retrying paid or high-volume tasks and monitor existing task IDs instead of resubmitting after timeouts.

## Reference(s):

- [Dataify Token Setup](references/token-setup.md)
- [Dataify Task Operations on ClawHub](https://clawhub.ai/dataify-server/skills/dataify-task-operations)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON task results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize large task results while preserving access to raw data.]

## Skill Version(s):

1.3.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
