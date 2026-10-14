## Description:

Helps agents scan OpenClaw skill folders locally with the ironheights CLI and explain suspicious findings before installation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[frank-masciopinto](https://clawhub.ai/user/frank-masciopinto)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and OpenClaw users review a skill folder for suspicious instructions before installing or enabling it, then decide how to handle the scanner's findings.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running an unpinned npm package may fetch code that has changed since review.

Mitigation: Verify the ironheights package and source before installation; pin a trusted version when appropriate.

Risk: An advisory scan can miss malicious content or report incomplete coverage; a hostile skill may try to influence an agent running the check.

Mitigation: Run the scanner outside the agent when possible, treat no findings as inconclusive, and review blocked, flagged or incomplete results before proceeding.

## Reference(s):

- [ironheights website](https://www.ironheights.dev)
- [ClawHub Malicious Skills Report, October 2026](https://www.ironheights.dev/reports/clawhub-malicious-skills-2026-10/)
- [ironheights on ClawHub](https://clawhub.ai/frank-masciopinto/skills/ironheights)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes verdicts, finding locations, skipped files and recommended next steps.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
