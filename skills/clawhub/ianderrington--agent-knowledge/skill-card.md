## Description:

Agent Knowledge Capture provides unified file-based capture and retrieval for URLs, video/article/paper extracts, social posts, and agent research outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ianderrington](https://clawhub.ai/user/ianderrington)

### License/Terms of Use:


## Use Case:

Developers and agents use this skill to save, index, search, and clean up reusable research notes, sourced claims, bookmarks, extracts, and social posts in a local markdown knowledge store.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores captured URLs, summaries, tags, and research notes persistently in the configured knowledge directory.

Mitigation: Review the configured knowledge directory before storing sensitive material and keep sensitive captures out of this store unless appropriate.

Risk: Automated cleanup with know tidy --fix can move files, normalize entries, and remove empty knowledge records.

Mitigation: Run tidy in audit mode first and enable heartbeat or cron cleanup only for a directory dedicated to this tool.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ianderrington/skills/agent-knowledge)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces guidance for creating and maintaining a local markdown knowledge store with YAML frontmatter and an auto-maintained index.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
