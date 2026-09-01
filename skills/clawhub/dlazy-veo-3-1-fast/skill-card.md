## Description:

Generates short text-to-video or image-to-video clips through Google Veo 3.1 Fast via the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to call dLazy's hosted video-generation API from a CLI workflow, providing prompts and optional media inputs to generate short video assets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local image or video inputs are sent to dLazy services for generation.

Mitigation: Avoid sensitive prompts and local media files unless the user is comfortable sending them to dLazy.

Risk: The skill uses a dLazy API key saved in local CLI configuration or supplied by environment variable.

Mitigation: Use user-scoped credentials and rotate or revoke the API key when it is no longer needed.

Risk: A persistent global CLI install may remain on the system after use.

Mitigation: Use the pinned npx invocation when a temporary, non-global CLI execution is preferred.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs or an async generateId; the --save option can download generated assets to a local path.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
