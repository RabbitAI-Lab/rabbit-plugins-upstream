## Description:

Helps operators write, publish, and manage articles, media, comments, themes, SEO, analytics, and paid-article settings on their awesome-poetize-open blog.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leapya](https://clawhub.ai/user/leapya)

### License/Terms of Use:

MIT-0

## Use Case:

Blog owners and administrators use this skill to plan and operate an awesome-poetize-open site, including publishing and recovering content and managing site settings. It does not support the closed-source POETIZE edition or other blogging platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A high-privilege API key or generated configuration may expose blog administration access.

Mitigation: Use a revocable least-privilege key, inject secrets securely or store them in a protected user config path, and do not commit credential files.

Risk: Publishing, deletion, uploads, theme or SEO changes, comments, and payment configuration can alter a live site or expose local files.

Mitigation: Require HTTPS and explicit confirmation of each target and action; inspect local image paths and payment settings, and preview drafts or edits before applying them.

Risk: The optional evaluation sends skill text to a user-selected external language-model endpoint.

Mitigation: Run evaluation only when intentionally opted in and after checking the destination and material to be sent.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/leapya/skills/awesome-poetize-open-blog-automation)
- [awesome-poetize-open project documentation](https://github.com/LeapYa/awesome-poetize-open)
- [Blog strategy playbook](references/strategy-playbook.md)
- [Content decision matrix](references/decision-matrix.md)
- [Creativity workflow](references/creativity-workflow.md)

## Skill Output:

**Output Type(s):** [Markdown, Text guidance, Shell commands, Configuration]

**Output Format:** [Markdown articles and guidance, shell commands, and JSON configuration]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May publish or change live blog content and settings after user confirmation.]

## Skill Version(s):

2.5.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
