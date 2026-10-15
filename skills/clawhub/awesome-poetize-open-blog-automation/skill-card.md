## Description:

Helps blog owners draft and manage articles, media, comments, settings, and payments on awesome-poetize-open blogs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[leapya](https://clawhub.ai/user/leapya)

### License/Terms of Use:

MIT-0

## Use Case:

Blog owners and content teams use this skill to prepare, publish, and maintain posts and administer an awesome-poetize-open blog. It does not support other blogging platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A high-privilege blog admin key can expose control of the blog or leak through generated configuration.

Mitigation: Use a revocable least-privilege key where available and keep credentials and generated configuration out of repositories.

Risk: Live-changing commands can run without an enforced confirmation gate.

Mitigation: Manually confirm each publish, delete, comment, theme, SEO, resource, taxonomy, or payment change before execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/leapya/skills/awesome-poetize-open-blog-automation)
- [Strategy playbook](references/strategy-playbook.md)
- [Decision matrix](references/decision-matrix.md)
- [Creativity workflow](references/creativity-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown articles, operational guidance, and structured JSON briefs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Drafts and changes to the live blog require review before execution.]

## Skill Version(s):

2.5.1 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
