## Description:

Publishes local Markdown notes and images as image-text posts through a user-configured MCP publishing backend, then checks the resulting note_id.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dqsjqian](https://clawhub.ai/user/dqsjqian)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to publish prepared Markdown copy and image files through a trusted MCP backend, including login checks, tag and image parsing, batch publishing, and note_id lookup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local note content and image files are sent to the configured MCP publishing backend.

Mitigation: Use only a backend you control or trust, and avoid publishing sensitive drafts or private media.

Risk: Batch publishing can publish every Markdown file in a directory without a confirmation or dry-run safeguard.

Mitigation: Check the target file or directory before running the skill, and test with a single note before using batch mode.

Risk: A wrong or untrusted backend URL can redirect publishing data to the wrong service.

Mitigation: Verify MCP_PUBLISHER_URL or config.json before running check or publish commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dqsjqian/skills/note-publisher)
- [README](artifact/README.md)
- [Skill definition](artifact/SKILL.md)
- [Example MCP configuration](artifact/config.example.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and command-line text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May emit NOTE_ID after a successful publish; the skill orchestrates publishing and does not generate note content.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
