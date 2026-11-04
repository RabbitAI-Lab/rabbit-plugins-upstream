## Description:

Reviews agent skills through static analysis, type-aware policies, scoring, and actionable improvement guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and skill authors use it to assess an existing agent skill, review quality and reliability, and get prioritized improvement guidance. Optional workflows support fix validation, local repairs, repository audits, and release checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publish-check mode may fetch and execute unpinned software, and publishing retries or release changes may proceed without clear approval.

Mitigation: Remove the automatic npx fallback and use a separately verified CLI version. Require explicit approval for the selected repository and publishing run before retries or release changes.

Risk: External CLI code and CI behavior were not verified in the security review.

Mitigation: Keep reviews limited to the selected skill or repository, and review the external CLI and CI behavior before enabling publish checks.

## Reference(s):

- [Project homepage](https://github.com/z-Zihan/awesome-skills)
- [ClawHub skill page](https://clawhub.ai/z-zihan/skills/skill-review-pro)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Files]

**Output Format:** [Markdown review reports with scores, findings, and prioritized recommendations; optional edits to selected skill files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a 100-point score, adversarial-check results, and optional fix or verification results.]

## Skill Version(s):

2.2.8 (source: release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
