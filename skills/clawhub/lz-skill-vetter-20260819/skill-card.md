## Description:

Skill Vetter audits OpenClaw skills for security, performance, and quality issues with rule-based scans, JSON reports, CI exit codes, exemptions, and severity-cap handling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zuoyunlai](https://clawhub.ai/user/zuoyunlai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill before installing or publishing OpenClaw skills to identify security, performance, and quality findings. It supports local scans, batch audits, human-readable reports, machine-readable JSON, and CI enforcement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Batch audits enumerate installed skill directories, and generated reports can include local file paths or snippets from scanned skills.

Mitigation: Prefer explicit target paths, review `scripts/batch_audit.sh` before batch use, and treat generated reports as potentially sensitive.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zuoyunlai/skills/lz-skill-vetter-20260819)
- [Audit Protocol](artifact/references/audit_protocol.md)
- [Output Format Reference](artifact/references/output_format.md)
- [Patterns Reference](artifact/references/patterns.md)
- [Rules Documentation](artifact/references/_rules_documentation.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or plain text with optional JSON audit reports and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may include findings, severity counts, verdicts, file paths, matched snippets, and CI exit codes.]

## Skill Version(s):

2.1.3 (source: server release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
