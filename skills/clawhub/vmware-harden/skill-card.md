## Description:

Helps operators audit VMware environments against compliance baselines, detect configuration drift, and review suggested remediations without directly changing managed systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure and security teams use this skill to scan vSphere, ESXi, and NSX environments against built-in or custom baselines, investigate drift, and produce compliance reports and remediation advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an unverified package or scanning with overly privileged accounts could expose infrastructure data.

Mitigation: Verify the package source and version before installation and use read-only service accounts for upstream collectors.

Risk: Local scan and audit databases contain sensitive infrastructure information.

Mitigation: Restrict access to the local DuckDB and audit database.

Risk: Optional AI advice may send violation evidence to Anthropic.

Mitigation: Set ANTHROPIC_API_KEY only when organizational policy permits sharing that evidence.

Risk: An exposed HTTPS MCP service could reveal compliance information to unauthorized callers.

Mitigation: Do not expose it without tokens, scoped roles, network restrictions, and token rotation.

Risk: Incomplete checks or missing collectors can make an empty violation list appear to show full compliance.

Mitigation: Review report coverage and scan status before reporting a target as compliant.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zw008/skills/vmware-harden)
- [Project homepage (listed in release metadata)](https://github.com/vmware-skills/VMware-Harden)
- [Setup guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Text or JSON compliance reports, drift findings, and suggested remediation steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports include scan coverage; remediation suggestions do not execute changes.]

## Skill Version(s):

1.14.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
