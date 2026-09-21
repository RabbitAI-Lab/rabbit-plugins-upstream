## Description:

Validate and ingest operator-pushed agent-bom inventory JSON from AWS, Azure, GCP, Snowflake, CMDB, or endpoint collectors for local findings, graph, policy, provenance, and auditor-ready exports without giving agent-bom direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, security engineers, and auditors use this skill when they already have canonical inventory JSON and need schema validation, local scanning, policy review, provenance checks, and exports for CI, graph, automation, or human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional enrichment can send selected inventory data to OSV or GitHub Advisory endpoints, and optional push can send data to an operator-provided control-plane URL.

Mitigation: Enable those network flows only when the operator has approved the destination and understands what inventory data will be used.

Risk: API tokens or URL credentials could be exposed if handled through chat or printed in logs.

Mitigation: Provide AGENT_BOM_API_KEY and push URLs through normal secret handling, and do not paste tokens into chat or display raw credentials.

Risk: Malformed inventory or missing trust fields can produce unreliable scan and provenance results.

Mitigation: Validate inventory against the packaged schema and require discovery_provenance and permissions_used before scanning.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/msaad00/skills/agent-bom-ingest)
- [agent-bom project homepage](https://github.com/msaad00/agent-bom)
- [agent-bom PyPI package](https://pypi.org/project/agent-bom/)
- [OSV vulnerability API](https://api.osv.dev/v1)
- [GitHub Advisory Database API](https://api.github.com/advisories)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Markdown, Code]

**Output Format:** [Markdown guidance with bash commands and export format choices]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce operator-selected JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX export files through agent-bom.]

## Skill Version(s):

0.105.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
