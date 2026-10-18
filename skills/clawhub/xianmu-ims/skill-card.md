## Description:

Helps users set up and manage their own XianMu IMS inventory through its MCP tools or REST API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaokingsoft](https://clawhub.ai/user/miaokingsoft)

### License/Terms of Use:

MIT-0

## Use Case:

Inventory owners and their assistants use this skill to connect to a self-hosted XianMu IMS instance, set up categories and locations, and manage items, stock movements, stocktakes, alerts, and documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory changes or deletions could alter records unexpectedly.

Mitigation: Review stock changes and deletion confirmations before proceeding; use read-only MCP mode for browsing.

Risk: An overly privileged API token could permit unintended changes.

Mitigation: Use the least-privilege token that supports the intended task and keep it private.

Risk: Installing unverified software or uploading unintended documents may expose data.

Mitigation: Verify the official installer and checksum; upload only documents or URLs intended for storage in the IMS instance.

## Reference(s):

- [Installation and connection guide](references/setup.md)
- [API endpoint reference](references/api.md)
- [Onboarding workflow](references/onboarding.md)
- [Onboarding scenarios](references/scenarios.md)
- [MCP tool reference](references/mcp-tools.md)
- [XianMu IMS API and MCP documentation](https://ims.miaoking.com/docs/api.html)
- [XianMu IMS deployment documentation](https://ims.miaoking.com/docs/deploy.html)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Text]

**Output Format:** [Markdown with commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use connected IMS tools to query or update the user's inventory after appropriate confirmation.]

## Skill Version(s):

1.1.0 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
