## Description:

Enables an agent to read Workday org charts, worker profiles, pay, benefits, performance, and task data through the user's signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Employees with authorized Workday access use the skill to look up reporting relationships, worker profiles, and HR records through their existing signed-in session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Reads confidential HR information, including pay, benefits, and performance data, through a live Workday session.

Mitigation: Use only with employer authorization and treat retrieved records as confidential; limit requests and sharing to the intended purpose.

Risk: Broad people and team triggers could access Workday when the user did not intend an HR lookup.

Mitigation: Confirm user intent before accessing Workday for ambiguous people or team requests.

Risk: Raw fetch and GraphQL reads can expose more sensitive information than a targeted lookup.

Mitigation: Prefer specific read tools and limit raw or GraphQL queries to the minimum fields needed.

## Reference(s):

- [workday-mcp on ClawHub](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Guidance, Configuration instructions]

**Output Format:** [Markdown guidance and structured JSON tool results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Workday results depend on the user's session and permissions.]

## Skill Version(s):

1.1.5 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
