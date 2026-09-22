## Description:

笔记 is a note-taking assistant that helps generate and organize structured notes using Cornell, Zettelkasten, mind-map, meeting, and classroom note formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and teams use this skill to convert class, meeting, and knowledge-management material into structured notes and reusable note outlines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the advertised note-taking purpose does not cleanly match task CLI, command execution, file writing, API key, and history logging behavior.

Mitigation: Review before installing; grant read/write/exec only in a constrained workspace and define allowed command, log, and storage locations.

Risk: The skill may process or log sensitive note content.

Mitigation: Avoid placing secrets or confidential content in notes unless the runtime, storage path, and logs are access-controlled and reviewed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/note-taker)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured note templates, outlines, concise confirmations, exported note data, and history logging guidance.]

## Skill Version(s):

1.0.0 (source: server release metadata; artifact frontmatter reports 2.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
