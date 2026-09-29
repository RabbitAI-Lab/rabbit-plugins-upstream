## Description:

Connects an agent to Todoist through Maton to manage tasks, projects, sections, labels, and comments with user-approved changes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Todoist users and developers can ask an agent to find, organize, create, update, complete, or delete tasks and related resources in their connected account. They can also configure user-approved automations through Maton.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Todoist changes or deletions may affect the wrong resource or cause data loss.

Mitigation: Start with read/list calls and confirm each write with the exact resource ID and intended effect.

Risk: Raw API keys may expose a long-lived credential.

Mitigation: Prefer Maton CLI login; use a raw API key only when the CLI cannot be used, and do not expose it in logs.

Risk: Hosted functions, triggers, and destinations can continue acting or forwarding events after setup.

Mitigation: Review their downstream effects and require separate explicit approval before enabling persistent automation or event forwarding.

## Reference(s):

- [Todoist skill on ClawHub](https://clawhub.ai/byungkyu/skills/todoist-api)
- [Todoist API v1 documentation](https://developer.todoist.com/api/v1)
- [Todoist filter syntax](https://todoist.com/help/articles/introduction-to-filters)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton CLI manual](https://cli.maton.ai/manual)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with command and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses an authorized Todoist connection; changes require explicit user approval.]

## Skill Version(s):

1.2.6 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
