## Description:

Storyboard helps create multi-shot animated shorts with consistent characters by using scripts, character and shot prompts, reference sheets, first and last frames, image-to-video shots, voice/TTS, music, sound effects, subtitles, and Remotion rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to run the dLazy storyboard template for project-scoped, multi-turn creation of animated short-video storyboards and related media-generation prompts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, options, and selected attachments may be sent to dLazy hosted services.

Mitigation: Review prompts and attachments for sensitive content before invocation, and avoid attaching files that should not leave the local environment.

Risk: The skill requires a dLazy API key that can be persisted in local CLI configuration.

Mitigation: Use the per-invocation DLAZY_API_KEY environment variable or npx execution path when reducing local persistence is preferred, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Installing or running the pinned npm package introduces normal third-party package supply-chain risk.

Mitigation: Review the @dlazy/cli package and source before installation, and prefer the pinned version declared by the release metadata.

Risk: The release depends on hosted API and media-storage endpoints for normal operation.

Mitigation: Confirm that api.dlazy.com and files.dlazy.com are acceptable for the deployment environment before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown-style terminal text with inline CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Responses are streamed through the dLazy CLI; attached local files may be uploaded to dLazy media storage when the user invokes file attachment options.]

## Skill Version(s):

1.3.13 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
