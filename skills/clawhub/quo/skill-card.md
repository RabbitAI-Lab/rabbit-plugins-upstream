## Description:

Helps agents use a connected Quo business phone account to manage calls, messages, contacts, and conversations through Maton.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams managing a Quo business phone account can ask an agent to review calls and conversations, retrieve recordings or transcripts, manage contacts, and send messages with approval. The skill also describes optional scheduled or event-driven automation through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Access to sensitive business phone messages, calls, contacts, and recordings.

Mitigation: Connect only the intended account, limit access to the current task, and avoid exposing unrelated records.

Risk: Sending SMS or deleting contacts can have external or irreversible effects.

Mitigation: Confirm the exact account, recipient or record, payload, and action before making changes.

Risk: Deployed functions, triggers, and webhooks can keep running or forwarding data.

Mitigation: Require separate approval for persistent automation, including its destination URL, payload, and intended duration.

## Reference(s):

- [Quo skill release on ClawHub](https://clawhub.ai/byungkyu/skills/quo)
- [Maton](https://maton.ai)
- [Quo API introduction](https://www.quo.com/docs/mdx/api-reference/introduction)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with command and code examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May summarize account data or propose actions and automation for user approval.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
