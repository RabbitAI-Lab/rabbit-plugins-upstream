## Description:

Helps users configure and manage inventory in their own Xianmu IMS instance, including item records, stock movements, stocktakes, alerts, and storage locations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[miaokingsoft](https://clawhub.ai/user/miaokingsoft)

### License/Terms of Use:

MIT-0

## Use Case:

People managing their own Xianmu IMS use this skill to set up categories and locations, look up inventory, record stock changes, conduct stocktakes, and manage related documents. Authorized users can work through their instance's MCP or REST interface.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Write-capable access can change inventory records and attached files.

Mitigation: Use a viewer token for lookup; grant member access only for intended writes and admin access only for initialization.

Risk: Deleting images or documents can be irreversible.

Mitigation: Review the target and obtain explicit user confirmation before deleting files or documents.

## Reference(s):

- [Source skill in server-resolved GitHub import](https://github.com/miaokingsoft/XianMuIMS/tree/main/skill/xianmu-ims)
- [ClawHub skill release](https://clawhub.ai/miaokingsoft/skills/xianmu-ims)
- [REST API reference](artifact/references/api.md)
- [MCP tool reference](artifact/references/mcp-tools.md)
- [Onboarding guide](artifact/references/onboarding.md)
- [Setup scenarios](artifact/references/scenarios.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Markdown with inventory summaries, setup plans, and example API requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [With authorization, the agent can make inventory and document changes in the user's IMS instance.]

## Skill Version(s):

0.1.0 (source: ClawHub release; bundled skill documentation: 1.0.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
