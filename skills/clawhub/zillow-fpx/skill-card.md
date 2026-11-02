## Description:

Query zillow.com (US real-estate portal) from a shell with the fpx CLI (@fetchproxy/cli) instead of running the zillow-mcp server — search listings, pull a full property record by zpid, price/tax/Zestimate history, photos, market reports, and your signed-in saved searches/homes, all via one-shot HTTP calls through a signed-in browser tab.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to query Zillow listings, property details, market reports, and signed-in saved data from shell workflows through a paired browser session.

### Deployment Geography for Use:

United States

## Known Risks and Mitigations:

Risk: Signed-in Zillow requests expose saved homes and searches to the agent.

Mitigation: Approve only Zillow access and the needed fetch capability, and revoke pairing when access is no longer needed.

Risk: Browser extension access and temporary fetched pages can affect account and data security.

Mitigation: Verify the extension release and protect temporary output files.

## Reference(s):

- [Zillow pages for fpx](references/pages.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ClawHub skill release](https://clawhub.ai/chrischall/skills/zillow-fpx)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration instructions, Guidance]

**Output Format:** [JSON data and Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live Zillow page data; saved searches and homes require a signed-in Zillow tab.]

## Skill Version(s):

1.2.5 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
