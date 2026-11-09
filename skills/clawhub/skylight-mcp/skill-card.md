## Description:

Connects an agent to a user's Skylight Calendar family hub to read and manage events, chores and rewards, shared lists, and meal plans.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Families using Skylight Calendar can ask an agent to retrieve and manage calendar events, chores and rewards, shared lists, and meal plans for their family hub.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation wording may route ordinary meal, chore, or shopping requests to the connected Skylight account.

Mitigation: Activate the skill only when the user clearly asks to use Skylight or its family hub.

Risk: The security scan was partial because two local references were unresolved.

Mitigation: Review the setup and activation instructions before connecting a Skylight account.

## Reference(s):

- [Skylight Calendar](https://www.ourskylight.com)
- [skylight-mcp on npm](https://www.npmjs.com/package/skylight-mcp)

## Skill Output:

**Output Type(s):** [Text, Structured data]

**Output Format:** [Natural-language summaries and Skylight calendar, chore, list, or meal data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can perform read and write actions on the connected Skylight family hub.]

## Skill Version(s):

1.6.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
