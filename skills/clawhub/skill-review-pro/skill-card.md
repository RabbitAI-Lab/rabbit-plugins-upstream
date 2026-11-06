## Description:

Evaluates agent skills through static analysis, type-aware policies, and a 100-point scoring model, then provides review reports and improvement suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:


## Use Case:

Developers and skill authors use it to assess skill quality and robustness, receive scored review findings, and plan improvements. Its companion fix flow applies changes only after user confirmation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Publication checks may automatically run downloaded software.

Mitigation: Before enabling publication checks, remove the automatic package-download fallback or configure a reviewed, installed CLI.

Risk: Publication workflows can initiate CI reruns or version changes and affect release state.

Mitigation: Require explicit approval for CI reruns and version changes, and retain confirmation of local edits.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/z-zihan/skills/skill-review-pro)
- [Project homepage](https://github.com/z-Zihan/awesome-skills)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance, Files]

**Output Format:** [Markdown review reports and improvement guidance, with optional skill-file edits after user approval.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fixes require user confirmation before changes are applied.]

## Skill Version(s):

2.2.9 (source: frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
