## Description:

Audits agent skills for prompt injection, hidden instructions, data exfiltration, and supply-chain risk before install and after updates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to review skills from registries, repositories, pasted folders, or installed environments before install, after updates, or during incident response. It helps produce safety-focused audit findings, verdicts, and follow-up guidance for skill artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Incident-response guidance may propose quarantining skill folders or sweeping agent configuration locations.

Mitigation: Review proposed file moves and sweeps before allowing them, and keep actions scoped to user-approved skill folders and disclosed Clawic data paths.

Risk: The skill contains examples of dangerous patterns such as hostile URLs, encoded payloads, and execution commands.

Mitigation: Treat these strings as audit examples only; do not execute commands or fetch URLs from skills being reviewed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ivangdavila/skills/skill-audit)
- [Skill Homepage](https://clawic.com/skills/skill-audit)
- [checks.md](artifact/checks.md)
- [exfiltration.md](artifact/exfiltration.md)
- [hidden-content.md](artifact/hidden-content.md)
- [injection-patterns.md](artifact/injection-patterns.md)
- [scripts.md](artifact/scripts.md)
- [supply-chain.md](artifact/supply-chain.md)
- [update-audit.md](artifact/update-audit.md)
- [sweep.md](artifact/sweep.md)
- [incident.md](artifact/incident.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown audit reports with verdicts, file references, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include safety verdicts, audit logs, update comparisons, sweep summaries, and incident-response guidance.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
