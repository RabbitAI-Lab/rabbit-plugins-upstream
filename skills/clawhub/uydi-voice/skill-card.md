## Description:

Uydi Voice lets agents design voices, clone voices from samples, synthesize speech, create sound scenes, and produce multi-voice audio with the Uydi platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lvyinchao](https://clawhub.ai/user/lvyinchao)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create and manage custom or cloned voices, synthesize narration, and assemble multilingual or multi-speaker audio with Uydi.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The cloning workflow may rely on assumed consent and adulthood for the voice sample.

Mitigation: Confirm that the voice owner is an adult and has authorized cloning before submitting a sample.

Risk: The security review did not fully evaluate every component of the release.

Mitigation: Review the skill files, especially the CLI script, before installing or using the skill.

Risk: Deleting a Voice Canvas or Sound Scene project permanently removes its stored audio.

Mitigation: Check the project ID and confirm the deletion is intended before running a delete command.

Risk: The installation guidance uses an unpinned package installation command.

Mitigation: Verify the selected package and release before installing it.

## Reference(s):

- [Uydi API and MCP installation guide](https://uydi.com/api-docs#install-mcp)
- [Voice discovery](references/voice-discovery.md)
- [Voice Canvas](references/voice-canvas.md)
- [Sound Scenes](references/sound-scenes.md)
- [Uydi homepage](https://uydi.com)

## Skill Output:

**Output Type(s):** [Audio files, Structured data, Guidance]

**Output Format:** [WAV audio, JSON project data, and text responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio generation and some voice or project operations use the user's Uydi credits.]

## Skill Version(s):

1.4.0 (source: SKILL.md frontmatter, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
