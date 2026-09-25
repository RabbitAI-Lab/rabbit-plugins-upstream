## Description:

Unified knowledge capture and retrieval for URLs, video/article/paper extracts, social posts, and agent research outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[space-cadet](https://clawhub.ai/user/space-cadet)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and agent operators use this skill to save, search, summarize, tag, and re-find useful URLs, extracts, social posts, and agent research outputs in a local knowledge store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill persists saved knowledge locally, which may retain secrets or sensitive private material if an agent stores them.

Mitigation: Review what the agent saves and avoid storing secrets or sensitive private material unless retention is intentional.

Risk: Automatic tidy operations can change files inside the knowledge directory.

Mitigation: Run cleanup in audit mode first and enable recurring tidy --fix jobs only when automatic normalization is acceptable.

Risk: The installed helper script is unaudited in the provided security evidence.

Mitigation: Review the installed helper script before deployment and monitor its file-system behavior in the configured knowledge directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/space-cadet/skills/knowledge)
- [Original ClawHub URL from artifact metadata](https://clawhub.ai/ianderrington/agent-knowledge)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with YAML frontmatter and command-line guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates and maintains local Markdown knowledge entries and an index in a configurable knowledge directory.]

## Skill Version(s):

1.0.0 (source: artifact metadata and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
