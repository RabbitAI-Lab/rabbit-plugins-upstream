## Description:

Discover restaurants on Tock via MCP, including city lists, metro search, venue details, bookable experiences, prices, party sizes, open dates and times, and signed-in reservation/profile checks when enabled.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to connect an agent to a local Tock MCP workflow for restaurant discovery, availability checks, and user-authorized reservation/profile lookups through a signed-in browser tab.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Account tools can access the user's Tock profile and reservation history through a signed-in browser tab.

Mitigation: Install and enable the workflow only when the user is comfortable granting that read access, and keep booking, cancellation, payment, and password handling outside the skill.

Risk: Reservation status can be misreported if an attempted booking is treated as confirmed before Tock account data catches up.

Mitigation: Use tock_verify_reservation for confirmation, re-query after a short delay when absence is inconclusive, and report attempts as unverified unless both external confirmation evidence and the verification tool agree.

Risk: The workflow depends on the user's browser session and may encounter sign-in or Cloudflare challenge states.

Mitigation: Resolve sign-in and challenge prompts directly in the browser tab before relying on account-specific tool results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chrischall/skills/tock-mcp)
- [tock-mcp source repository](https://github.com/chrischall/tock-mcp)
- [tock-mcp npm package](https://www.npmjs.com/package/tock-mcp)
- [fetchproxy browser extension](https://github.com/chrischall/fetchproxy)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include MCP tool names, setup snippets, availability summaries, and reservation verification guidance.]

## Skill Version(s):

0.3.0 (source: server release metadata and release changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
