## Description:

Trello API integration with managed OAuth for managing boards, lists, cards, members, labels, and related project-management resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[byungkyu](https://clawhub.ai/user/byungkyu)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to authenticate through Maton and perform Trello project-management tasks such as listing boards, creating or updating cards, managing lists, and setting up approved automations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read and modify Trello data through the user's authorized Maton connection.

Mitigation: Use OAuth when possible, connect only the Trello account needed, default to read/list calls, and get explicit approval before each write.

Risk: Functions, triggers, and destinations can keep running or forwarding data after setup.

Mitigation: Review and approve each function, trigger, and destination separately, disclose what data will flow where, and delete automations that are no longer needed.

Risk: Raw HTTP mode requires handling a long-lived Maton API key when the CLI cannot be installed.

Mitigation: Prefer the Maton CLI with OAuth; when raw HTTP is necessary, keep the API key out of logs, command output, files, and shared destinations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/byungkyu/skills/trello-api)
- [Maton homepage](https://maton.ai)
- [Maton documentation](https://docs.maton.ai)
- [Maton API reference](https://docs.maton.ai/api-reference/overview)
- [Maton CLI manual](https://cli.maton.ai/manual)
- [Trello API overview](https://developer.atlassian.com/cloud/trello/rest/api-group-actions/)
- [Trello boards API](https://developer.atlassian.com/cloud/trello/rest/api-group-boards/)
- [Trello lists API](https://developer.atlassian.com/cloud/trello/rest/api-group-lists/)
- [Trello cards API](https://developer.atlassian.com/cloud/trello/rest/api-group-cards/)
- [Trello checklists API](https://developer.atlassian.com/cloud/trello/rest/api-group-checklists/)
- [Trello labels API](https://developer.atlassian.com/cloud/trello/rest/api-group-labels/)
- [Trello members API](https://developer.atlassian.com/cloud/trello/rest/api-group-members/)
- [Trello search API](https://developer.atlassian.com/cloud/trello/rest/api-group-search/)
- [Time trigger reference](references/time/triggers.md)
- [Calendly trigger reference](references/calendly/triggers.md)
- [GitHub trigger reference](references/github/triggers.md)
- [Gmail trigger reference](references/google-mail/triggers.md)
- [HubSpot trigger reference](references/hubspot/triggers.md)
- [Linear trigger reference](references/linear/triggers.md)
- [Notion trigger reference](references/notion/triggers.md)
- [Slack trigger reference](references/slack/triggers.md)
- [Stripe trigger reference](references/stripe/triggers.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON examples, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires network access, a Maton account, and user approval for Trello connections, writes, functions, triggers, and destinations.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
