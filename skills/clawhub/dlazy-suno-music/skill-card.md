## Description:

Helps agents generate vocal or instrumental music with automatic or user-provided lyrics through the dLazy Suno Music service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request songs with generated or custom lyrics, including instrumental tracks, and retrieve the resulting audio.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an external CLI introduces third-party code.

Mitigation: Review the pinned dLazy CLI package and its source before installing.

Risk: The CLI stores an API key locally and sends prompts and supplied files to dLazy services.

Mitigation: Protect and rotate the key as needed; avoid submitting sensitive prompts or files.

Risk: Music generation may consume paid credits.

Mitigation: Check the cost estimate with dry-run and confirm available credits before generating.

Risk: The bundled output example labels an image, not audio.

Mitigation: Confirm the returned media type and URL before presenting or saving the result as audio.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-suno-music)
- [dLazy CLI documentation and source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown with command examples and links to generated audio]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return a hosted audio URL or an asynchronous task ID; downloaded audio is optional.]

## Skill Version(s):

1.3.23 (source: ClawHub release metadata; bundled skill frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
