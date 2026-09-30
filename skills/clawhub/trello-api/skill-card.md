## Description:

Helps agents manage Trello boards, lists, cards, checklists, labels, and members through a user-authorized Maton connection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

People and teams managing projects use this skill to inspect Trello work and, with explicit approval, update boards, lists, cards, and related resources. It can also guide user-approved automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A connected account allows access to and changes in Trello data.

Mitigation: Trust the integration before connecting, limit account access, and explicitly approve each write.

Risk: Raw API keys can expose long-lived credentials.

Mitigation: Prefer the CLI OAuth flow; use raw API keys only when the CLI cannot be installed.

Risk: Functions, triggers, and destinations can continue acting or forwarding data after setup.

Mitigation: Approve each automation and destination separately, and review or remove them when no longer needed.

## Reference(s):

- [ClawHub Trello skill](https://clawhub.ai/byungkyu/skills/trello-api)
- [Maton homepage](https://maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Trello API documentation](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/)
- [Maton time trigger reference](artifact/references/time/triggers.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Code, Guidance]

**Output Format:** [Markdown with CLI examples and structured API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Trello access requires a user-authorized connection; writes and automations require explicit approval.]

## Skill Version(s):

1.2.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
