## Description:

Vaaya lets agents use a single MCP server to call paid APIs pay-per-call across search, scraping, media generation, sandboxes, browser automation, communications, enrichment, and live data with per-call spend caps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[marupelkar](https://clawhub.ai/user/marupelkar)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use Vaaya to connect an agent to a prepaid API marketplace through MCP, then consult the live catalog and execute paid API calls with explicit spend caps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enables broad paid API access from a prepaid wallet and can spend account credit.

Mitigation: Set clear spending limits, require explicit human approval before paid actions, and use the per-call max_cost_cents cap returned by consult.

Risk: The skill can trigger externally impactful actions such as outreach, scraping, browser automation, sandbox jobs, hosting, storage changes, or contacts with third parties.

Mitigation: Require explicit user approval before those actions and review the planned service, action, parameters, and cost cap before calling use.

Risk: Refresh tokens provide durable access to the Vaaya account.

Mitigation: Store refresh tokens only in private agent state or a secret store, avoid logs and shared repositories, and revoke access if exposure is suspected.

## Reference(s):

- [Vaaya homepage](https://vaaya.ai/?utm_source=clawhub&utm_medium=agent&utm_campaign=skill)
- [Vaaya MCP endpoint](https://vaaya.ai/mcp)
- [Vaaya services and pricing](https://vaaya.ai/services?utm_source=clawhub&utm_medium=agent&utm_campaign=skill)
- [Vaaya agent-readable index](https://vaaya.ai/llms.txt)
- [Vaaya full tool reference](https://vaaya.ai/llms-full.txt)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with bash commands and JSON API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes OAuth setup guidance, consult-use-result usage flow, and spend-cap handling guidance.]

## Skill Version(s):

1.2.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
