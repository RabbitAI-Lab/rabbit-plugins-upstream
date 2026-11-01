## Description:

Reviews agent skills through static analysis, scores their quality, and provides actionable improvement recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use it to assess an agent skill’s quality and robustness, receive a scored review with improvement guidance, and verify fixes or publication status.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publication checks may automatically download and run a CLI through an npx fallback.

Mitigation: Before using publication checks, remove the automatic npx fallback or configure an explicitly selected, trusted CLI version.

Risk: Proposed file changes could introduce incorrect or misleading guidance.

Mitigation: Review and scan proposed changes before applying them, especially added translations.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/z-zihan/skills/skill-review-pro)
- [Project homepage](https://github.com/z-Zihan/awesome-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown review reports and prioritized recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a 100-point score; response language follows the user. Fixes require explicit user confirmation.]

## Skill Version(s):

2.2.4 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
