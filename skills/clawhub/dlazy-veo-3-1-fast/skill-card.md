## Description:

Generates short text-to-video or image-to-video clips with Google Veo 3.1 Fast through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's pinned CLI for fast Google Veo 3.1 Fast video generation from prompts, optional frame images, or videos to extend.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on a third-party npm CLI that handles prompts, API keys, and user-provided media.

Mitigation: Use the pinned npx invocation when possible, review the linked package/source before use, and install only when the dLazy CLI is trusted for the intended data.

Risk: Prompts and local media paths supplied to generation commands are sent to dLazy API and file-hosting endpoints.

Mitigation: Avoid sending sensitive prompts or media unless the service terms and organization policy allow it.

Risk: The dLazy API key may be stored in local CLI configuration.

Mitigation: Prefer least-privilege operational handling, protect the local config file, and rotate or revoke the key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs, a saved local asset path, or an asynchronous generation ID for later polling.]

## Skill Version(s):

1.3.14 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
