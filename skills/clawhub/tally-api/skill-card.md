## Description:

Guides agents in managing Tally forms, submissions, workspaces, organization membership, and webhooks through a connected Maton account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Tally users and developers use this skill to inspect and manage forms, submissions, workspaces, webhooks, and organization access, with explicit approval before changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Changes to forms or organization membership can alter data or account access.

Mitigation: Confirm the connected account, target resource or person, and intended effect before approving each write.

Risk: Webhooks and automated destinations can repeatedly send submission data, including personal information, to external URLs.

Mitigation: Confirm the destination owner and URL, the data sent, and whether forwarding persists before creating webhooks, functions, or triggers.

Risk: Shared trigger references for other apps could be mistaken for Tally capabilities.

Mitigation: Use non-Tally event sources only when the user explicitly requests and authorizes that separate integration.

## Reference(s):

- [Tally skill release](https://clawhub.ai/byungkyu/skills/tally-api)
- [Maton](https://maton.ai)
- [Tally API introduction](https://developers.tally.so/api-reference/introduction)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Time trigger reference](references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Configuration guidance]

**Output Format:** [Markdown with inline shell and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read and list by default; obtain explicit user approval before writes or automation setup.]

## Skill Version(s):

1.2.4 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
