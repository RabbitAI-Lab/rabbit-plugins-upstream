## Description:

HuanZhi FA Pro helps Chinese startup founders assess fundraising readiness, analyze term-sheet risks, and practice investor negotiation with Capital EQ guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-innopower](https://clawhub.ai/user/ai-innopower)

### License/Terms of Use:

MIT-0

## Use Case:

External founders and startup operators use this skill to evaluate fundraising readiness, identify risky financing terms, prepare negotiation responses, and receive emotional support around fundraising decisions. The skill is informational and does not replace legal, financial, or investment professionals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Founder profiles, business plans, and term-sheet materials may be stored locally and can contain sensitive company information.

Mitigation: Use only redacted documents unless local storage, retention, and deletion behavior are acceptable for the deployment environment.

Risk: The artifact claims a passed security audit, while the authoritative security evidence reports a suspicious verdict and says that claim should not be treated as verified.

Mitigation: Review the skill before installing and do not rely on the audit claim without independent confirmation.

Risk: Memory, reminders, and broad triggers can preserve or resurface sensitive fundraising context.

Mitigation: Limit stored profile data and reminder content to non-sensitive summaries, or disable those capabilities where confidentiality requirements are strict.

Risk: Financing, legal, and negotiation guidance may be incomplete or unsuitable for a specific transaction.

Mitigation: Treat outputs as informational support and consult qualified legal, financial, or investment professionals for key decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/ai-innopower/skills/huanzhi-fa-skill-pro)
- [Publisher Profile](https://clawhub.ai/user/ai-innopower)
- [Output Schema](artifact/references/outputs-schema.md)
- [Configuration Guide](artifact/references/config-guide.md)
- [Failure Handling](artifact/references/failure-handling.md)
- [Known Limitations](artifact/references/known-limitations.md)
- [Determinism Details](artifact/references/determinism-details.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and structured JSON reports, with optional shell commands for the local funding diagnosis script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Financing diagnosis and term-sheet analysis outputs are expected to follow documented JSON schemas and self-validation behavior.]

## Skill Version(s):

2.9.5 (source: server release metadata, SKILL.md frontmatter, skill.json, CHANGELOG released 2026-08-25)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
