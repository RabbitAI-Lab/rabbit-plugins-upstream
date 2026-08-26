## Description:

Technical Article Writer guides agents through an interview-driven workflow for drafting technical articles and blog posts for developer audiences, including idea sharpening, title and hook generation, structure, drafting, editing, image suggestions, and title finalization.

This skill is ready for commercial/non-commercial use.

## Publisher:

[samber](https://clawhub.ai/user/samber)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, engineers, and technical content creators use this skill to turn technical topics into structured developer-facing articles. It supports the workflow from intake questions and angle selection through title options, article structure, draft markdown, edits, image suggestions, and final title alternatives.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated technical articles may contain inaccurate claims, weak code examples, or misleading recommendations if user-provided context is incomplete.

Mitigation: Review the draft for technical accuracy, test any code snippets, and verify quantitative claims before publication.

Risk: Midjourney prompt guidance may become stale because it depends on current external model documentation.

Mitigation: Check current Midjourney documentation before using generated prompt parameters.

Risk: The workflow can delegate hook, CTA, or humanizing steps to other writing skills when available, which may compound stylistic or factual errors.

Mitigation: Review the final combined output for factual accuracy, tone, attribution, and fit with the intended audience.

## Reference(s):

- [Technical Article Writer on ClawHub](https://clawhub.ai/samber/skills/technical-article-writer)
- [Project Homepage](https://github.com/samber/cc-skills)
- [Article Structures Reference](artifact/references/article-structures.md)
- [Hooks and Titles Reference](artifact/references/hooks-and-titles.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Markdown article drafts with titles, body sections, optional code snippets, image suggestions, optional image prompts, and title alternatives.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May ask intake questions before drafting and may recommend review of current external documentation for Midjourney prompt advice.]

## Skill Version(s):

1.3.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
