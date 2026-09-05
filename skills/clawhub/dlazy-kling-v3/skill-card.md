## Description:

Powerful video generation with Kling v3, supporting text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Kling v3 videos from text prompts or reference images through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected local media can be uploaded to dLazy's hosted service for generation.

Mitigation: Use only prompts and media appropriate for dLazy-hosted processing, and review the service terms before sending sensitive content.

Risk: Generated output URLs are hosted by dLazy.

Mitigation: Treat returned media links according to the user's sharing and retention requirements before redistributing them.

Risk: Login stores a revocable dLazy API key in the local CLI configuration.

Mitigation: Protect the local config file, prefer per-invocation credentials when needed, and rotate or revoke the key if exposure is suspected.

Risk: A global CLI install persists the broader dLazy command surface on the host.

Mitigation: Use the pinned npx invocation when a non-persistent CLI is preferred, and review CLI commands before using workflows outside Kling v3.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI commands and JSON responses with generated media URLs or optional saved files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous generation IDs, polling, timeout control, dry-run cost estimates, and optional local save paths.]

## Skill Version(s):

1.3.12 (source: server release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
