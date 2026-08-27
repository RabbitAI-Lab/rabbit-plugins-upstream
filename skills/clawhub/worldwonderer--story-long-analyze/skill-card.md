## Description:

Analyzes long-form Chinese web novels through a staged deconstruction pipeline covering the opening chapters, character structure, payoff design, pacing, settings, relationships, summary reporting, and prose style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Writers, editors, and story-development agents use this skill to analyze novels the user lawfully possesses and turn them into structured markdown notes about plot, pacing, characters, settings, reusable writing patterns, and style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill saves the full novel text and generated analysis locally.

Mitigation: Use it only with works the user lawfully possesses and when local retention of the text and analysis is acceptable.

Risk: Optional backfill and maintenance flows can modify existing analysis or planning files.

Mitigation: Review prompts and target paths before allowing optional backfill into planning files or rewrites of existing indexes.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/worldwonderer/skills/story-long-analyze)
- [OpenClaw Source Metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Deconstruction Notes](references/deconstruction-notes.md)
- [Material Decomposition](references/material-decomposition.md)
- [Output Templates](references/output-templates.md)
- [Pipeline Operations](references/pipeline-ops.md)
- [Style Profile Generator](references/style-profile-generator.md)
- [Style Profile Protocol](references/style-profile-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands, Configuration]

**Output Format:** [Markdown files, progress notes, concise prompts, and implementation guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes local analysis artifacts and may copy the provided source text into the configured local analysis directory.]

## Skill Version(s):

1.1.17 (source: ClawHub release evidence; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
