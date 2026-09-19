## Description:

Manage Trello boards, lists, and cards via the Trello REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[azizbrownint](https://clawhub.ai/user/azizbrownint)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to inspect Trello boards, lists, and cards and to propose Trello REST API commands for creating, moving, commenting on, and archiving cards.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Trello API key and token give the agent live access to a Trello account.

Mitigation: Use the narrowest Trello token permissions available, keep tokens out of logs, and avoid sharing command histories that include credentials.

Risk: Create, move, comment, and archive examples can change important boards when executed.

Mitigation: Confirm write commands before execution and test against non-critical boards when possible.

## Reference(s):

- [ClawHub Trello Skill](https://clawhub.ai/azizbrownint/skills/trello)
- [Trello REST API documentation](https://developer.atlassian.com/cloud/trello/rest/)
- [Trello API key page](https://trello.com/app-key)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires curl, jq, TRELLO_API_KEY, and TRELLO_TOKEN.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
