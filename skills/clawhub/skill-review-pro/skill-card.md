## Description:

Reviews AI agent skills through static analysis and produces a scored report with improvement suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill maintainers use it to assess skill quality and robustness, produce a 100-point review with prioritized suggestions, and optionally validate fixes or release contents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publication checks may download executable software through an automatic package fallback and restart jobs that publish changes without separate approval.

Mitigation: Disable the automatic package fallback, use a reviewed CLI version, and require separate approval for CI reruns or publishing changes.

Risk: Repairs may change reviewed skill content or fail to preserve its language requirements.

Mitigation: Review the displayed diff before accepting repairs and check that the target skill's language is preserved.

## Reference(s):

- [Project homepage](https://github.com/z-Zihan/awesome-skills)
- [ClawHub release page](https://clawhub.ai/z-zihan/skills/skill-review-pro)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Code]

**Output Format:** [Markdown review reports and recommendations; optional skill file edits and text verification results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [100-point scoring with prioritized findings and improvement suggestions]

## Skill Version(s):

2.2.7 (source: SKILL.md frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
