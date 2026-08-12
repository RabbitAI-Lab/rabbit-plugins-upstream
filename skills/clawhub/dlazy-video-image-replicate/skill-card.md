## Description:

Studies a user-provided reference image or video, then helps recreate the same look and structure with the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to route reference-based image or video recreation requests to the dLazy hosted agent through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Attached local files are uploaded to dLazy media storage and may contain private or sensitive content.

Mitigation: Attach only files intended for upload and review file paths before invoking the CLI with file attachments.

Risk: Authentication can persist an API key or session data in local CLI configuration.

Mitigation: Use npx or the DLAZY_API_KEY environment variable for ephemeral use, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Continuing an existing project can send prompts into the wrong saved project context.

Mitigation: List projects and confirm the target project id before using continuation commands.

Risk: The security verdict flags privacy and local-permission concerns around the dLazy CLI workflow.

Mitigation: Review the dLazy CLI before installation and prefer per-invocation execution when a persistent global binary is not required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI source link from metadata](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [Publisher profile](https://clawhub.ai/user/dlazyai)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown and terminal-oriented guidance with CLI commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream hosted agent responses and may reference uploaded user files when the CLI is invoked with file attachments.]

## Skill Version(s):

1.3.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
