## Description:

VMware Harden helps agents audit VMware vSphere, ESXi, and NSX environments against security baselines, detect drift, and produce remediation advice, reports, and dashboard output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zw008](https://clawhub.ai/user/zw008)

### License/Terms of Use:

MIT

## Use Case:

Developers, platform engineers, and security operators use this skill to run point-in-time VMware compliance scans, review drift, inspect baseline coverage, and obtain remediation suggestions without directly changing the target estate.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence reports that the skill is mostly read-only but documentation inconsistently mentions a remediation apply path that could lead agents toward changes outside the declared scope.

Mitigation: Use this skill for scanning, reports, drift, and advice only; route actual remediation through approval-gated vmware-pilot and do not allow a harden apply workflow unless the installed package's approval gates and pilot handoff have been independently confirmed.

Risk: Advisor output can use an external Anthropic API call when ANTHROPIC_API_KEY is configured.

Mitigation: Leave ANTHROPIC_API_KEY unset for offline-only use, or review which violation evidence may be sent externally before enabling live LLM advice.

Risk: An empty violation list can be mistaken for a clean compliance verdict when collector coverage is incomplete.

Mitigation: Review the coverage and undetermined-rule fields before reporting scan results, and avoid calling an estate compliant when checks were not evaluated.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zw008/skills/vmware-harden)
- [Project homepage](https://github.com/vmware-skills/VMware-Harden)
- [Setup Guide](references/setup-guide.md)
- [CLI Reference](references/cli-reference.md)
- [Capabilities](references/capabilities.md)
- [Agent Guardrails](references/agent-guardrails.md)
- [Cross-Skill Workflows](references/cross-skill-workflows.md)
- [vSphere 9 STIG content sync](references/stig-content-sync.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with CLI commands, configuration snippets, and structured compliance report summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May refer to local DuckDB state and coverage metadata when summarizing scan and drift results.]

## Skill Version(s):

1.10.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
