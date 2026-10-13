## Description:

Helps audit VMware environments against compliance baselines, investigate configuration drift, and suggest remediation without changing managed systems.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Infrastructure and security teams use this skill to scan vSphere, ESXi, and NSX configurations against built-in or custom baselines, review compliance findings and coverage, and investigate drift. Remediation is suggested, not executed by this skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Compliance evidence and drift history remain in a local database.

Mitigation: Confirm local storage is permitted and protect access to the evidence database.

Risk: Optional AI advice sends structured violation evidence to Anthropic.

Mitigation: Set ANTHROPIC_API_KEY only if organizational policy permits sharing that evidence.

Risk: Incomplete scan coverage could be mistaken for a clean compliance result.

Mitigation: Review coverage and snapshot details before making compliance claims; rescan if evidence is missing or stale.

Risk: Remediation suggestions could lead to unreviewed infrastructure changes.

Mitigation: Review suggestions and use vmware-pilot's approval-gated workflow for actual remediation; keep related packages pinned and reviewed.

## Reference(s):

- [ClawHub release](https://clawhub.ai/zw008/skills/vmware-harden)
- [Project homepage (declared in skill metadata)](https://github.com/vmware-skills/VMware-Harden)
- [Setup guide](artifact/references/setup-guide.md)
- [Cross-skill remediation workflow](artifact/references/cross-skill-workflows.md)

## Skill Output:

**Output Type(s):** [Compliance findings, Reports, Remediation guidance, Shell commands, Configuration guidance]

**Output Format:** [Text, Markdown, and structured JSON reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports should identify the scan snapshot and any checks that could not be evaluated.]

## Skill Version(s):

1.11.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
