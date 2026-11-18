## Description:

Use when creating a Hindsight-docs-style local documentation skill for another tool, SDK, API, or docs repository.

This skill is ready for commercial/non-commercial use.

## Publisher:

[theangrypit](https://clawhub.ai/user/theangrypit)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to scaffold a local documentation skill for another tool, SDK, API, or repository, after mapping the repository's documentation paths.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review is benign with medium confidence and incomplete reference checks; it also advises checking that the reported GitHub installer behavior and file and shell capabilities fit the intended use.

Mitigation: Review the selected source paths and generator behavior, then scan the generated bundle before executing or installing it.

## Reference(s):

- [Docs Skill Model](references/docs-skill-model.md)
- [ClawHub release page](https://clawhub.ai/theangrypit/skills/docs-skill-builder)

## Skill Output:

**Output Type(s):** [Files, Markdown, Shell commands, Guidance]

**Output Format:** [A local source folder with a shell generator, a generated SKILL.md, and mirrored documentation references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Selected documentation files are copied verbatim; the generated bundle includes source and mirror hash manifests.]

## Skill Version(s):

1.0.4 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
