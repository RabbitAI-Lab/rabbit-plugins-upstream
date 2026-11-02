## Description:

Audits VMware vSphere, ESXi, and NSX environments against security baselines, detects configuration drift and known vulnerabilities, and provides remediation advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and infrastructure security engineers use this skill to scan VMware environments against compliance baselines, review drift and known vulnerabilities, and prepare remediation recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scan results may contain sensitive environment and violation details.

Mitigation: Protect stored scan results and limit access to the local data store and its backups.

Risk: Optional Anthropic advice may share violation evidence externally.

Mitigation: Enable external AI advice only when sharing that evidence is acceptable.

Risk: Remediation suggestions may be unsuitable for the environment.

Mitigation: Review remediation plans before approving execution.

Risk: Exposing the dashboard remotely can make scan results accessible beyond the local host.

Mitigation: Keep the dashboard local unless remote access is secured.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-harden)
- [Project homepage](https://github.com/vmware-skills/VMware-Harden)
- [Setup guide](references/setup-guide.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [vSphere 9 STIG content sync](references/stig-content-sync.md)

## Skill Output:

**Output Type(s):** [Text, JSON, CSV, Markdown, Shell commands, Guidance]

**Output Format:** [Compliance findings, coverage and drift summaries, vulnerability status, remediation advice, and commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scan results include coverage context; remediation is advice and requires separate approval-gated execution.]

## Skill Version(s):

1.18.0 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
