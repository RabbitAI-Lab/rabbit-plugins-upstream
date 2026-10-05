## Description:

Helps agents query US Redfin listings, property details, market trends, rentals, climate risk, photos, and optionally saved account data through a user-approved browser bridge.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve US real-estate listings and property information from Redfin using shell commands instead of a running MCP server. Signed-in users can also request saved homes and searches.

### Deployment Geography for Use:

Global (US real-estate data)

## Known Risks and Mitigations:

Risk: Pairing the browser bridge enables requests through the user's current Redfin session.

Mitigation: Approve pairing only if comfortable granting this access, and use a trusted Redfin browser tab.

Risk: Saved homes and searches may expose private account data to the shell, logs, and downstream tools.

Mitigation: Avoid signed-in saved-data workflows unless needed; limit access to command output and logs when used.

Risk: Redfin may substitute an indexed region or cap listing results, making a search incomplete or misleading.

Mitigation: Check the returned region and narrow broad searches with filters.

## Reference(s):

- [Redfin endpoint examples](references/stingray-endpoints.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)
- [ContextMint Bridge source](https://github.com/nullnet-app/contextmint-bridge)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Redfin responses can be parsed as JSON after removing the response prefix; saved account data requires a signed-in browser tab.]

## Skill Version(s):

1.1.8 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
