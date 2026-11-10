## Description:

Audits VMware vSphere, ESXi, and NSX environments against security baselines, detects configuration drift and known vulnerabilities, and provides remediation advice.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and VMware administrators use this skill to assess compliance, baseline status, configuration drift, and known advisories across VMware environments, and to review suggested remediation steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial because some local references could not be resolved, so referenced material may be outside the reviewed evidence.

Mitigation: Review the setup guidance and referenced material that was not included in the scan before installing.

Risk: The setup guidance includes Docker image and uvx references that are not pinned, so the resolved software can change over time.

Mitigation: Review the installation source and pin a trusted image digest or package version before deployment.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/zw008/skills/vmware-harden)
- [Project homepage](https://github.com/vmware-skills/VMware-Harden)
- [Setup guide](artifact/references/setup-guide.md)
- [CLI reference](artifact/references/cli-reference.md)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, JSON, CSV, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Compliance and drift reports, structured findings, and remediation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Point-in-time findings and suggestions; remediation is not executed by this skill.]

## Skill Version(s):

1.19.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
