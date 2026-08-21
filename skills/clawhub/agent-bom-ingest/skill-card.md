## Description:

Validates and ingests operator-pushed agent-bom inventory JSON from cloud, CMDB, endpoint, or AI-agent sources so users can generate local findings, graphs, policy, provenance, and auditor-ready exports without direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security engineers, and auditors use this skill to validate canonical agent-bom inventory and produce local scan findings, graph and policy context, provenance checks, and export artifacts without granting direct cloud credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Untrusted or malformed inventory can produce misleading scan findings or exports.

Mitigation: Validate inventory against the packaged inventory.schema.json contract before treating it as evidence or generating outputs.

Risk: Optional control-plane push can send inventory data to the wrong endpoint if configured carelessly.

Mitigation: Use AGENT_BOM_PUSH_URL only for an explicitly chosen operator-owned destination and provide AGENT_BOM_API_KEY through environment variables, not chat.

Risk: Optional vulnerability enrichment can contact external services.

Mitigation: Use network enrichment only when calls to OSV and GitHub Advisory endpoints are approved for the environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-ingest)
- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [OSV vulnerability API](https://api.osv.dev/v1)
- [GitHub Advisory Database API](https://api.github.com/advisories)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and export format recommendations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports operator-selected JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX export paths through agent-bom commands.]

## Skill Version(s):

0.101.0 (source: server release, frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
