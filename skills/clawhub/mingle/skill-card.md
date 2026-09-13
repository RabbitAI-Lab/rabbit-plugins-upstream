## Description:

Mingle helps agents find people for professional networking by publishing approved cards, searching shared cards, and managing introductions with user approval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[aeoess](https://clawhub.ai/user/aeoess)

### License/Terms of Use:

MIT-0

## Use Case:

External users and their agents use Mingle to find professional contacts, publish approved networking cards, request introductions, and exchange contact details only when both sides approve.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external MCP server and the Mingle API for networking workflows.

Mitigation: Install only when comfortable with external network access, prefer pinned setup commands, and review the package and service links before enabling it.

Risk: The skill stores a local identity key and can perform session-start inbox checks if background checks are enabled.

Mitigation: Leave background checks off unless wanted, and review local Mingle settings before enabling automatic checks.

Risk: Published cards, introduction notes, and contact lines can disclose professional or personal details.

Mitigation: Review every exact preview before confirmation and avoid confidential, third-party, contact, or sensitive details unless intentionally shared.

## Reference(s):

- [Mingle ClawHub release](https://clawhub.ai/aeoess/skills/mingle)
- [aeoess publisher profile](https://clawhub.ai/user/aeoess)
- [Mingle MCP npm package](https://www.npmjs.com/package/mingle-mcp)
- [Mingle homepage](https://aeoess.com/mingle)
- [Mingle API](https://api.aeoess.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown or plain text with exact previews, search results, introduction states, and configuration snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [State-changing actions require a preview-confirm flow with an approved digest.]

## Skill Version(s):

4.0.1 (source: server release metadata and artifact _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
