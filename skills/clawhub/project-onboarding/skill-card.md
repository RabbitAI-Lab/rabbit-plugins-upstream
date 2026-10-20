## Description:

Helps experienced developers get up to speed on an unfamiliar project through staged, evidence-based guidance on its structure, workflows, and development practices.

This skill is ready for commercial/non-commercial use.

## Publisher:

[z-zihan](https://clawhub.ai/user/z-zihan)

### License/Terms of Use:

MIT-0

## Use Case:

Experienced developers use this skill to orient themselves in a local frontend, backend, desktop, mini-program, or mobile project and identify how to start developing safely. It presents a concise overview first, then offers deeper project-specific guidance on request.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Repository inspection could read files outside the intended project.

Mitigation: Use a confirmed local project path and keep read-only inspection within that repository, without following links outside it.

Risk: The optional Git clone flow accesses an external repository.

Mitigation: Clone only with explicit user confirmation, check the source, use a temporary directory, and clean up afterward.

## Reference(s):

- [ClawHub project-onboarding release](https://clawhub.ai/z-zihan/skills/project-onboarding)
- [Publisher-listed project homepage](https://github.com/z-Zihan/awesome-skills)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Bilingual, staged guidance grounded in repository evidence; pauses for confirmation before deeper analysis.]

## Skill Version(s):

2.0.4 (source: skill frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
