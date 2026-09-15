## Description:

VMware Harden helps agents run point-in-time VMware compliance scans, baseline checks, drift detection, remediation advice, and dashboard/report workflows for vSphere, ESXi, and NSX environments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and security teams use this skill to audit VMware environments against CIS, vSphere SCG, STIG-aligned, PCI-DSS, BSI IT-Grundschutz, EU NIS2, and custom baselines. It is suited for scan, report, drift, and remediation-planning workflows, not automatic unsupervised changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence flags inconsistent documentation around an apply path that can trigger real VMware changes through other skills.

Mitigation: Use the skill for scans, reports, drift, and advice only unless a human intentionally chooses the remediation extras and vmware-pilot approval workflow; do not allow automatic vmware-harden apply calls.

Risk: Live remediation advice can send selected violation context to Anthropic when ANTHROPIC_API_KEY is configured.

Mitigation: Review data-sharing policy before enabling live advice, and leave ANTHROPIC_API_KEY unset when external LLM calls are not approved.

Risk: Empty violation results can be misread as a clean compliance verdict when collector coverage is incomplete.

Mitigation: Check the returned coverage fields and report undetermined rules, missing node attributes, and stale snapshots before summarizing compliance posture.

## Reference(s):

- [VMware Harden homepage](https://github.com/vmware-skills/VMware-Harden)
- [Agent guardrails](references/agent-guardrails.md)
- [Capabilities](references/capabilities.md)
- [CLI reference](references/cli-reference.md)
- [Cross-skill workflows](references/cross-skill-workflows.md)
- [Setup guide](references/setup-guide.md)
- [vSphere 9 STIG content sync](references/stig-content-sync.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and occasional JSON or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include compliance findings, coverage caveats, drift summaries, and remediation suggestions; does not by itself confirm that an estate is compliant.]

## Skill Version(s):

1.10.9 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
