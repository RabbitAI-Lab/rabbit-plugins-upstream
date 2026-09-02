## Description:

Discover restaurants on Tock via MCP, including city lists, metro search, venue details, bookable experiences, prices, party sizes, and open dates or times.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to let an agent discover Tock restaurants, inspect availability, and check signed-in account reservations while leaving booking and payment on exploretock.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires running the tock-mcp npm package and the fetchproxy browser extension.

Mitigation: Install only after reviewing those components and confirming the local environment is appropriate for running them.

Risk: Signed-in account tools can read the user's Tock profile and reservation history.

Mitigation: Use signed-in account tools only when profile, reservation, or verification checks are needed, and treat their access as read-only.

Risk: A Tock booking attempt outside the tools can appear successful before it is actually confirmed.

Mitigation: Require captured confirmation evidence and a confirmed result from tock_verify_reservation before reporting a booking as confirmed.

## Reference(s):

- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp)
- [tock-mcp source repository](https://github.com/chrischall/tock-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-mcp)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration]

**Output Format:** [Markdown with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for MCP tool setup and use; Tock account tools are described as read-only and require a signed-in browser tab.]

## Skill Version(s):

0.4.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
