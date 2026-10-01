## Description:

Validates operator-provided agent-bom inventory JSON and guides local scanning and export of findings, graphs, policy, and provenance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to validate operator-supplied agent inventories and produce local findings and auditor-ready exports without providing cloud credentials to agent-bom.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory and exported findings may contain sensitive information.

Mitigation: Scan only intended inventory files and handle exported results as sensitive.

Risk: An optional control-plane push may send inventory data to an unintended destination.

Mitigation: Verify the operator-provided destination before pushing and keep API tokens in environment variables, not chat.

Risk: Untrusted or malformed inventory can lead to misleading findings.

Mitigation: Validate against the packaged schema and stop if required provenance or permissions fields are missing.

## Reference(s):

- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)
- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-ingest)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance and commands; optional JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3.11+, agent-bom 0.84.4+, and inventory JSON conforming to the packaged schema.]

## Skill Version(s):

0.107.0 (source: server-resolved release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
