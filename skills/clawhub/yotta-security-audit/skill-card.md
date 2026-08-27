## Description:

元安 yotta-security-audit helps agents run read-only security audits for AI skill directories and Windows/Linux system baselines, then report suspicious patterns and recommended next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, security reviewers, and agent operators use this skill before installing or during auditing of agent skills to scan for malicious patterns, supply-chain risks, and local system baseline issues. It is intended for authorized targets only and reports findings without performing repair, deletion, or quarantine actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad or global installation can copy the scanner into more agent skill folders than intended.

Mitigation: Install only into the intended agent or directory, preferably with --agent or --dir instead of global mode.

Risk: System baseline mode may inspect sensitive local security files and configuration on the machine where it runs.

Mitigation: Run system-level scans only on machines you administer and are comfortable exposing to local security inspection.

Risk: Scanner findings can include context-dependent signals such as network calls, high-entropy strings, URLs, or installation hooks.

Mitigation: Review findings manually, prioritize high and critical severities, and confirm whether each signal is expected for the audited target.

## Reference(s):

- [Threat Patterns](references/threat-patterns.md)
- [Remediation Guide](references/remediation-guide.md)
- [System Baseline Checks](references/system-baseline.md)
- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-security-audit)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Plain text, JSON, or Markdown reports with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports are read-only audit results with severity levels, locations, descriptions, and recommended follow-up actions.]

## Skill Version(s):

0.1.4 (source: frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
