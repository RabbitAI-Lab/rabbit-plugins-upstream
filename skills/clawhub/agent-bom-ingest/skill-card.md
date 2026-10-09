## Description:

Validates operator-provided agent inventory JSON and guides local scanning and export without requiring direct cloud credentials.

This skill is ready for commercial/non-commercial use.

## Publisher:

[msaad00](https://clawhub.ai/user/msaad00)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to validate inventory supplied by their own collectors, scan it locally for findings, and prepare exports for security or audit workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected inventory files could contain sensitive data or secrets.

Mitigation: Limit access to the intended inventory file, and verify redaction before including secrets or sharing exports.

Risk: Optional advisory lookups or control-plane push can transmit data over the network.

Mitigation: Enable network lookups only when appropriate; push only to an operator-approved destination with its designated authentication method.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/msaad00/skills/agent-bom-ingest)
- [agent-bom project homepage (declared in skill metadata)](https://github.com/msaad00/agent-bom)
- [agent-bom package (declared in skill metadata)](https://pypi.org/project/agent-bom/)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides validation and local scanning; the invoked tool can write operator-selected JSON, SARIF, HTML, or Markdown exports.]

## Skill Version(s):

0.108.3 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
