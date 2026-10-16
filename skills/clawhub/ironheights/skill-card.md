## Description:

Helps users review OpenClaw skills by scanning their files locally and explaining security findings before the skills are trusted.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frank-masciopinto](https://clawhub.ai/user/frank-masciopinto)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and developers use this skill to check a skill's local files for suspicious instructions before installing or trusting it, and to review findings after updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An unverified or unpinned scanner package could introduce supply-chain risk.

Mitigation: Verify the intended npm package and linked project before installation; prefer a vetted pinned version over unpinned npx.

Risk: The optional update check contacts npm and ClawHub and may update the scanner.

Mitigation: Review update behavior before use, or disable updates with IRONHEIGHTS_NO_UPDATE=1 when network access or automatic changes are not acceptable.

Risk: A scan with no findings may still miss malicious behavior or be incomplete.

Mitigation: Treat the verdict as advisory, review skipped files, and independently inspect the skill before trusting it.

## Reference(s):

- [Ironheights website](https://www.ironheights.dev)
- [ClawHub Malicious Skills Report](https://www.ironheights.dev/reports/clawhub-malicious-skills-2026-10/)
- [Ironheights on ClawHub](https://clawhub.ai/frank-masciopinto/skills/ironheights)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with scan verdicts, findings, and next steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Advisory; findings identify the rule, file, and line when available.]

## Skill Version(s):

1.2.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
