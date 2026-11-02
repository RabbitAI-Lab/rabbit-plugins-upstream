## Description:

Scales engineering care to the risk of a software change, keeping small edits light and adding evidence, compatibility and recovery checks as risk grows. Use when writing, fixing, debugging, reviewing, refactoring or shipping code, configuration, schemas and migrations, infrastructure, user interfaces, or LLM and agent features in a software project, including casual add, fix or build requests. Not for prose, slides, explanations, summaries or standalone snippets outside a project.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ricardodpalmeida](https://clawhub.ai/user/ricardodpalmeida)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use Whetstone to scale engineering guidance and verification to the risk of software changes in a project.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The optional change scanner is heuristic, so a clean result does not establish security.

Mitigation: Run it in the intended project repository, review findings in context, and keep consequential actions within approved scope.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ricardodpalmeida/skills/whetstone)
- [Testing](references/testing.md)
- [Security](references/security.md)
- [Data and privacy](references/data-and-privacy.md)
- [Delivery and release](references/delivery-and-release.md)
- [AI features](references/ai-features.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Markdown, Shell commands, Analysis]

**Output Format:** [Task-specific code changes, engineering guidance, Markdown plans or review notes, and optional scanner text or JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the project task; the optional scanner reports heuristic findings.]

## Skill Version(s):

0.3.5 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
