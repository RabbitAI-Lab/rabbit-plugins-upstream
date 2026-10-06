## Description:

Validates operator-provided agent-bom inventory JSON and guides local scanning and export of findings without requiring direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security teams use this skill to validate operator-generated inventory, inspect local findings, and prepare graph, policy, or audit exports without giving the scanner cloud credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using an untrusted scanning tool or malformed inventory could yield unreliable findings.

Mitigation: Confirm you trust agent-bom and validate the inventory against its packaged schema before scanning.

Risk: Optional control-plane push could disclose inventory or expose an API token.

Mitigation: Review inventory before pushing, use only an operator-controlled destination, and keep tokens in environment variables rather than chat.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/msaad00/skills/agent-bom-ingest)
- [Project homepage (skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom package](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Files]

**Output Format:** [Markdown guidance and commands; optional JSON, SARIF, HTML, Markdown, CycloneDX, or SPDX exports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires schema-valid inventory; exports are written only to operator-selected paths.]

## Skill Version(s):

0.108.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
