## Description:

Applies NIST/CWE security hardening to Python and Rust code.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and security engineers use this skill to perform repository-wide security hardening audits for Python and Rust code, map findings to NIST SSDF and CWE references, and prepare concrete remediation proposals for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository-wide scanning can inspect a large amount of local code and produce remediation proposals that may change security-sensitive behavior.

Mitigation: Keep initial runs in report-only mode, review each proposal and citation, and approve changes one finding at a time.

Risk: Auto-apply mode or approved proposals can create commits or GitHub-facing artifacts.

Mitigation: Enable auto-apply only after reviewing a report, keep critical findings behind explicit approval, and rerun project gates after each applied change.

## Reference(s):

- [harden skill page on ClawHub](https://clawhub.ai/athola/skills/nm-pensive-harden)
- [ClawDIS metadata homepage: claude-night-market/pensive](https://github.com/athola/claude-night-market/tree/master/plugins/pensive)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports with findings tables, remediation proposals, shell commands, code and configuration snippets, and optional commits or GitHub-facing artifacts after approval.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [First runs should remain report-only; approved changes are intended to be applied one finding at a time with validation gates.]

## Skill Version(s):

1.9.19 (source: ClawHub release metadata; artifact frontmatter reports 1.9.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
