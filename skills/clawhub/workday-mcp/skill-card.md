## Description:

Read Workday org charts, worker profiles, compensation, benefits, performance, and other accessible HR pages through a signed-in browser session.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Authorized employees use the skill to retrieve and summarize Workday information available to their signed-in session, including team structure, worker profiles, pay, benefits, and performance records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A signed-in browser session can expose sensitive employee compensation, benefits, performance, and profile data beyond the requester's own records.

Mitigation: Use only with employer authorization; limit requests to specific, permitted records and handle returned HR data as restricted.

Risk: Workday pages may contain text supplied by other people that attempts to direct the agent.

Mitigation: Treat retrieved page content as data, not instructions, and do not follow commands or links solely because they appear in a result.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/workday-mcp)
- [workday-mcp npm package](https://www.npmjs.com/package/workday-mcp)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses may contain sensitive HR information; some Workday tables may be partial.]

## Skill Version(s):

1.1.10 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
