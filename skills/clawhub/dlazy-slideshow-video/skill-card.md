## Description:

Turns slides or documents into narrated slideshow videos with voiceover and transitions through the dLazy hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn presentations, documents, images, and prompts into narrated slideshow-style videos through the pinned dLazy CLI and hosted file-to-video agent.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and explicitly attached files may be sent to dLazy hosted endpoints for processing.

Mitigation: Use only with content approved for upload to dLazy, and avoid attaching secrets or sensitive documents unless that transfer is authorized.

Risk: The dLazy CLI can save an API key in the local user configuration.

Mitigation: Protect the local config file, prefer one-off npx execution when a persistent global binary is not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on npm or npx and network access to dLazy API and file-storage endpoints.

Mitigation: Confirm npm or npx availability, authentication, balance, and endpoint access before relying on the skill in an operational workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-slideshow-video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses a pinned dLazy CLI command flow; attached local files are uploaded to dLazy media storage before hosted processing.]

## Skill Version(s):

1.0.15 (source: server release evidence; artifact frontmatter shows 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
