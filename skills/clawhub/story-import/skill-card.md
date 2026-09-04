## Description:

Reverse-imports an existing Chinese-language novel manuscript into a standard writing-project structure for continued use with story-long-write or story-short-write workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT-0

## Use Case:

Authors and writing-workflow agents use this skill to turn an existing draft or completed manuscript into a reusable writing project with source analysis, settings, outline, body text, and tracking assets for future continuation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads manuscript content supplied by the user.

Mitigation: Install and run it only for manuscripts the user intends the agent to process, and avoid providing confidential text unless the execution environment is appropriate for that content.

Risk: The skill can create or update local writing-project files, including archiving old tracking state and setting the active imported book.

Mitigation: Review target paths before confirming import, especially when an existing project already has tracking files or an active-book marker.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/worldwonderer/skills/story-import)
- [OpenClaw source metadata](https://github.com/zenstory-ai/oh-story-claudecode)
- [Character state reverse rules](artifact/references/character-state-reverse.md)
- [Length routing rules](artifact/references/length-routing.md)
- [Long-form structure mapping](artifact/references/structure-mapping-long.md)
- [Short-form structure mapping](artifact/references/structure-mapping-short.md)
- [Tracking transaction protocol](artifact/references/tracking-transaction.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with file paths, structured project artifacts, JSON state, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces or updates a local writing-project directory and analysis library from user-provided manuscript content.]

## Skill Version(s):

1.0.20 (source: ClawHub release evidence; skill frontmatter version: 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
