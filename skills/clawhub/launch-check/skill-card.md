## Description:

Launch readiness check and launch checklist for the current GitHub repository. Scores it 0-100 by fixed rules (README clarity, install line, licence, releases, CI, activity), shows the three fixes worth the most, offers to make them locally, and only if the human says yes, lists the project on ScBee.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hmakt99](https://clawhub.ai/user/hmakt99)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and repository maintainers use this skill to assess launch readiness and identify the highest-value fixes for a public GitHub repository or a public website. It presents a score and prioritized checklist before any optional local changes or public listing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence notes an unresolved reference to a token file at the repository root, leaving the assessment incomplete.

Mitigation: Before installing, inspect the referenced path and confirm what it contains and how the skill uses it.

## Reference(s):

- [ScBee](https://scbee.vercel.app)
- [ClawHub launch-check release](https://clawhub.ai/hmakt99/skills/launch-check)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Files]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Readiness score and band with prioritized fixes; local file changes only after user approval.]

## Skill Version(s):

1.0.2 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
