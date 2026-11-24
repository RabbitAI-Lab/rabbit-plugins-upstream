## Description:

Analyzes user-provided short web fiction into a structured Chinese-language deconstruction report covering story premise, plot structure, emotional arc, reversals, character functions, reusable techniques, and quality checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[9438190](https://clawhub.ai/user/9438190)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and story analysts use this skill to deconstruct short-form popular fiction they are allowed to analyze, producing reusable structure, technique, character, and quality notes for downstream writing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill tells the agent to continue analysis despite sensitive fictional content, which could conflict with higher-priority safety requirements.

Mitigation: Apply platform and system safety policies first, and review analysis requests before processing content that may be disallowed.

Risk: The workflow saves full source text and reports locally, which can retain private or copyrighted material.

Mitigation: Use only text the user is allowed to analyze, avoid private material unless local retention is acceptable, and delete generated source backups and reports when they are no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/9438190/skills/story-short-analyze)
- [OpenClaw Metadata Source](https://github.com/worldwonderer/oh-story-claudecode)
- [Output Contract](references/output-contract.md)
- [Output Templates](references/output-templates.md)
- [Short Fiction Decomposition Methodology](references/material-decomposition.md)
- [Quality Checklist](references/quality-checklist.md)
- [Genre Catalog](references/genre-catalog.md)
- [AI Tone and Banned-Words Checks](references/anti-ai-writing.md)
- [Banned Words](references/banned-words.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Guidance]

**Output Format:** [Chinese-language Markdown reports plus JSON metadata files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a source-text backup, deconstruction report, plot-node report, writing-technique report, and _meta.json under a story-specific output directory.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter says 3.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
