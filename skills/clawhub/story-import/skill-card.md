## Description:

Reverse-imports an existing novel or draft into a standard continuation-ready writing project, routing long-form and short-form works through the matching analysis and migration flow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers and writing-assistant agents use this skill to convert an already written or partially written novel into a structured project with source analysis, settings, outlines, draft text, and continuation state. It supports follow-on long-form or short-form writing workflows after import.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The import workflow can delegate work to project-local custom agents when deployment metadata is missing or mismatched, allowing untrusted project files to influence the import.

Mitigation: Install only in trusted story projects, verify the .story-deployed marker and custom agent files before using helper agents, or run in solo/direct mode when provenance is unclear.

Risk: The skill can create and modify writing-project files, archive older tracking files, and run bundled Python or Node validation tools.

Mitigation: Review the target project state before import, keep recoverable backups or version control, and inspect the generated changes and validation results before continuing writing work.

## Reference(s):

- [OpenClaw source metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Character State Reverse](references/character-state-reverse.md)
- [Format and Structure](references/format-and-structure.md)
- [Length Routing](references/length-routing.md)
- [State Tracking](references/state-tracking.md)
- [Structure Mapping Long](references/structure-mapping-long.md)
- [Structure Mapping Short](references/structure-mapping-short.md)
- [Tracking Initialization](references/tracking-initialization.md)
- [Tracking Transaction](references/tracking-transaction.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown project files, JSON tracking transactions, shell command guidance, and validation results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or modify project files, archive older tracking files, and invoke bundled Python or Node validation utilities.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata; artifact frontmatter: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
