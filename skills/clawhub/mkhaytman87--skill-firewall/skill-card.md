## Description:

Skill Firewall helps agents reduce prompt-injection risk from external skills by analyzing legitimate purpose, rewriting clean skill content, and requiring approval before saving.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mkhaytman87](https://clawhub.ai/user/mkhaytman87)

### License/Terms of Use:


## Use Case:

Developers and agent users use this skill to apply a cautious review-and-rewrite workflow before installing or using skills from external sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may add friction by treating most external-skill requests as security-sensitive.

Mitigation: Use it where external skill content is involved and expect a review-and-approval step before saving rewritten content.

Risk: A rewritten skill can omit useful behavior if the legitimate purpose is misunderstood.

Mitigation: Review the generated report and clean rewrite before approval, especially for trusted or complex source skills.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/mkhaytman87/skills/skill-firewall)
- [Project Homepage](https://github.com/openclaw/skill-firewall)

## Skill Output:

**Output Type(s):** [Markdown, Code, Guidance]

**Output Format:** [Markdown report with rewritten skill content and an approval prompt]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include suspicious-element notes and clean skill rewrites before any save action.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
