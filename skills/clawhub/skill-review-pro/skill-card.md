## Description:

Evaluates agent skills through static review, scoring, and type-aware policies, then provides a professional review report and improvement guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use it to assess an agent skill's quality and robustness, receive a score and specific improvement suggestions, or check a repository and verify a ClawHub release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: ClawScan reports a suspicious verdict with medium confidence. The publish-check workflow requires network access and may automatically fetch and run a package; analysis was partial because some referenced paths could not be resolved.

Mitigation: Do not install until comfortable with the network access and automatic package-fetch behavior; resolve and review the referenced paths and verify the complete release contents first.

## Reference(s):

- [Project repository](https://github.com/z-Zihan/awesome-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown review report with scores, findings, and improvement recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The response follows the user's language; optional repository audit or publish-verification results may be included.]

## Skill Version(s):

2.3.0 (source: SKILL.md frontmatter, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
