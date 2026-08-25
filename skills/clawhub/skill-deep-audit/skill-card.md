## Description:

Generic skill-quality auditor for agent skills that runs deterministic static or dry-run checks across seven dimensions and produces a scored Markdown audit report with findings and fix guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[songhonglei](https://clawhub.ai/user/songhonglei)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to audit agent skill directories before release, checking process closure, portability, usability, security posture, code quality, dependency footprint, and repeatability. The skill is intended for pre-ship quality review and produces a scorecard plus prioritized remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Routine audits can create local artifacts in the audited skill directory despite the skill's read-only framing.

Mitigation: Run the skill only where creation of AUDIT-*.md and possible Python cache files is acceptable, and review generated files before committing or publishing.

Risk: --fix mode can mutate audited skill files.

Mitigation: Treat --fix as a separate mutation workflow; require explicit item-level approval and confirm that a backup exists before edits proceed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/songhonglei/skills/skill-deep-audit)
- [Check rules](references/check-rules.md)
- [Controlled-domain list](references/controlled-domains.md)
- [Audit report output template](references/output-template.md)
- [Scan command reference](references/scan-commands.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown scorecard with a concise text summary and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routine audits write AUDIT-{YYYY-MM-DD}.md in the audited skill directory; --fix mode may edit files only after explicit approval and backup.]

## Skill Version(s):

1.1.0 (source: server release evidence, README changelog, and SKILL.md body)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
