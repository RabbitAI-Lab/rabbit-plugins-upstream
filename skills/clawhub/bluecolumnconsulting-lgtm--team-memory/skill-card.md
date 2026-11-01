## Description:

Team context memory \u2014 who does what, who knows what, and how the team actually works.

This skill is ready for commercial/non-commercial use.

## Publisher:

[bluecolumnconsulting-lgtm](https://clawhub.ai/user/bluecolumnconsulting-lgtm)

### License/Terms of Use:

MIT-0

## Use Case:

Teams and the agents that support them use this skill to store and retrieve role ownership, team strengths, communication preferences, working agreements, and onboarding context.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist identifiable team, member, and workstyle information to an external API.

Mitigation: Use only with organizational approval, avoid sensitive or evaluative personnel details unless authorized, and confirm retention, deletion, and access controls before deployment.

Risk: The skill requires a BlueColumn API key for all operations.

Mitigation: Store the API key in an approved secret manager or environment variable and do not paste it into prompts, logs, or shared documents.

## Reference(s):

- [BlueColumn API documentation](https://bluecolumn.ai/docs)
- [ClawHub skill page](https://clawhub.ai/bluecolumnconsulting-lgtm/skills/team-memory)
- [Publisher profile](https://clawhub.ai/user/bluecolumnconsulting-lgtm)

## Skill Output:

**Output Type(s):** [guidance, shell commands, API calls, markdown]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a BlueColumn API key and sends team-memory text to an external API.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
