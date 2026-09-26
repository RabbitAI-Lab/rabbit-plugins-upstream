## Description:

Exports reader comments from the currently signed-in WeChat Official Account into local, article-grouped Markdown with a JSON summary.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fatmind](https://clawhub.ai/user/fatmind)

### License/Terms of Use:

MIT-0

## Use Case:

WeChat Official Account operators can archive and review reader comments from their own signed-in account, organized by article for curation and feedback analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exported comments may contain personal reader information.

Mitigation: Store the output in a protected location and limit access to authorized readers.

Risk: Reader comments may render as active Markdown, including remote resources.

Mitigation: Open exports in a viewer that blocks remote resources; escape Markdown metacharacters before sharing or publishing.

Risk: The package includes an unrelated, under-documented LLM relay helper.

Mitigation: Review before installation; remove the helper if unnecessary or document it and restrict its endpoint to loopback.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/fatmind/skills/gzh-comment-export)

## Skill Output:

**Output Type(s):** [Markdown, JSON]

**Output Format:** [Local article-grouped comments.md and summary index.json, plus a one-line JSON status on stdout]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes comment author, content, time and region when available; index.json reports totals and partial-export status.]

## Skill Version(s):

1.0.0 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
