## Description:

Monitor Dataify Builder tasks through completion, recover safely after interruption, and guide cross-platform DATAIFY_API_TOKEN setup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dataify-server](https://clawhub.ai/user/dataify-server)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to monitor existing or newly submitted Dataify Builder tasks, retrieve final JSON results, resume safely after timeouts or interruptions, and configure DATAIFY_API_TOKEN without exposing the token.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires DATAIFY_API_TOKEN and can guide persistent shell configuration, which may store the token in a shell profile or user environment.

Mitigation: Never paste the token into chat, verify only whether the environment variable is present, and use persistent setup only when the user accepts local storage.

Risk: Task parameters, preview output, provider errors, or downloaded results may contain private targets or sensitive collected data.

Mitigation: Redact tokens and sensitive values, summarize large results, and avoid exposing private result contents in logs or shared messages.

Risk: Retrying paid, high-volume, or media tasks after a timeout or interruption may duplicate cost or work.

Mitigation: Resume monitoring with the same task ID and ask for confirmation before retrying paid or high-volume tasks.

## Reference(s):

- [Dataify Token Setup](references/token-setup.md)
- [Dataify Task Operations on ClawHub](https://clawhub.ai/dataify-server/skills/dataify-task-operations)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON task results and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include summarized task results, provider error details, safe retry guidance, and exact resume commands; large raw results should remain accessible without being fully pasted.]

## Skill Version(s):

1.3.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
