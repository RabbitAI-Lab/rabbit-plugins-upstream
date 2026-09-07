## Description:

Watch any social video -> get an architecture diagram, working component, runnable notebook, or step-by-step cheat sheet - automatically.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sonpiaz](https://clawhub.ai/user/sonpiaz)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill when a user provides a social video URL and wants the content summarized, implemented, converted into an architecture diagram, turned into a React component or notebook, or captured as a step-by-step cheat sheet.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI downloads videos and stores processed video artifacts and transcripts in a local archive.

Mitigation: Use it only for video sources and content that are appropriate to store locally, and review or clear the archive according to local data-handling expectations.

Risk: Extracted audio is uploaded to Kyma API for transcription by default.

Mitigation: Avoid sending sensitive audio to the transcription service, or use the documented local transcription mode when remote upload is not acceptable.

Risk: Optional browser-cookie access can use a local platform session for a specific run.

Mitigation: Do not enable browser-cookie access unless the user explicitly opts in and understands the session-access implications.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sonpiaz/skills/watch-cli)
- [watch-cli homepage](https://github.com/sonpiaz/watch-cli)
- [Install watch-cli v0.3.4](https://github.com/sonpiaz/watch-cli/releases/download/v0.3.4/install.sh)
- [Prompt templates](https://github.com/sonpiaz/watch-cli/tree/main/prompts)
- [Output schema](https://github.com/sonpiaz/watch-cli/blob/main/docs/output-schema.md)
- [Exit codes](https://github.com/sonpiaz/watch-cli/blob/main/docs/exit-codes.md)
- [Archive documentation](https://github.com/sonpiaz/watch-cli/blob/main/docs/archive.md)
- [Kyma API](https://kymaapi.com/?src=skill:watch)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or JSON-backed agent responses derived from video frames and transcript text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce project files, diagrams, React components, notebooks, or step-by-step cheat sheets depending on user intent.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
