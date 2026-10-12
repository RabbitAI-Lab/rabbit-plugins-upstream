## Description:

Helps experienced developers onboard an unfamiliar project through staged, evidence-based guidance tailored to its project type.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Experienced developers use this skill to understand an unfamiliar repository's structure, development workflow, and project-specific practices before making changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Analysis may expose sensitive files in the selected project.

Mitigation: Point the skill only at the intended project directory and exclude unrelated secrets.

Risk: An explicitly requested remote repository clone may introduce untrusted content.

Mitigation: Prefer a local checkout; if cloning is necessary, use a trusted repository URL and a temporary directory.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/z-zihan/skills/project-onboarding)
- [Skill homepage listed in metadata](https://github.com/z-Zihan/awesome-skills)

## Skill Output:

**Output Type(s):** [Markdown, Guidance, Shell commands]

**Output Format:** [Staged Markdown guidance with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Pauses after each stage for follow-up questions.]

## Skill Version(s):

2.0.3 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
