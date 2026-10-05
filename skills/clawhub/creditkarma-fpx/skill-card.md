## Description:

Guides agents through capturing a signed-in Credit Karma session with fpx and using curl to retrieve transactions without the MCP server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to obtain Credit Karma transaction data in shell scripts without installing the Credit Karma MCP server. It requires an existing signed-in browser session and the fpx/ContextMint bridge.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bridge can read Credit Karma session cookies, and captured access and refresh tokens can grant account access.

Mitigation: Use a trusted machine, avoid shared shells and logs, and remove bridge site access or unpair it when finished.

Risk: Transaction responses and temporary files may expose sensitive financial information.

Mitigation: Restrict access to any saved output and promptly remove temporary response files.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/chrischall/skills/creditkarma-fpx)
- [Transaction request examples](references/requests.md)
- [ContextMint Bridge releases](https://github.com/nullnet-app/contextmint-bridge/releases)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes transaction pagination and token-refresh guidance.]

## Skill Version(s):

3.1.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
