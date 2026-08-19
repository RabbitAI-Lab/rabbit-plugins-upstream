## Description:

PKULaw enables agents to search and retrieve laws, regulations, legal provisions, and judicial case records through an OOMOL-connected PKULaw account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and legal operations teams use this skill to run PKULaw legal searches and retrieve provisions or case documents from a connected PKULaw account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The generic PKULaw tool-call path could expose actions whose schema is not clearly read-only.

Mitigation: Inspect the live schema before using call_tool, run only clearly read-only actions directly, and ask for explicit confirmation before any action that appears to change, post, delete, or affect an account.

Risk: PKULaw legal-search results may be incomplete, outdated, or require professional interpretation.

Mitigation: Treat retrieved laws, provisions, and case documents as source material for review rather than final legal advice.

## Reference(s):

- [ClawHub PKULaw Skill](https://clawhub.ai/oomol/skills/oo-pkulaw)
- [PKULaw Homepage](https://mcp.pkulaw.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses may include PKULaw legal-search results as JSON.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
