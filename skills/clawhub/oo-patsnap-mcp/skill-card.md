## Description:

Patsnap MCP helps agents access Patsnap patent search, patent records, patent landscape analysis, and design FTO workflow actions through the OOMOL Patsnap MCP connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve and analyze Patsnap patent data, including search results, legal status, patent families, citations, full text, PDFs, images, valuation-related records, and patent landscape summaries. It can also guide design FTO workflow actions when the user has connected Patsnap MCP through OOMOL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes direct execution of remote installer scripts, which the security evidence flags as a supply-chain risk.

Mitigation: Review the oo CLI installer before running setup, download it from OOMOL, verify the source or checksum when available, and execute it only after inspection.

Risk: Some Patsnap MCP actions are tagged as write actions and can change service state.

Mitigation: Confirm the exact payload and intended effect with the user before allowing a write action to run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-patsnap-mcp)
- [Patsnap MCP homepage](https://open.patsnap.com/marketplace/mcp-servers)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; write actions require user confirmation.]

## Skill Version(s):

1.0.1 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
