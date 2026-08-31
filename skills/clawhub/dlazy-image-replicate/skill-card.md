## Description:

Image replicate tool: analyzes the visuals, composition, colors, lighting, and style of the source image, builds a replicate prompt, and hands it off to Seedream 4.5 to generate a new image in the same style.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke the dLazy image-replication service from an agent workflow, sending reference images and prompt parameters to generate a new image with similar composition, color, lighting, and style.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files are sent to dLazy cloud endpoints for inference and storage.

Mitigation: Review cloud-service use before installing, and avoid sending media or prompts that should not leave the local environment.

Risk: The skill stores a dLazy API key in local CLI configuration, and the security evidence says the inspected CLI package does not appear to enforce the user-only file permissions claimed by the skill text.

Mitigation: Prefer per-invocation DLAZY_API_KEY where practical, rotate or revoke keys from the dLazy dashboard when needed, and verify permissions on ~/.dlazy/config.json after login.

Risk: A global CLI installation persists a binary on the system.

Mitigation: Use the pinned npx @dlazy/cli@1.2.3 invocation path when a non-global installation is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-replicate)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image URLs or an asynchronous generation ID; the CLI can also save generated assets to a local path.]

## Skill Version(s):

1.3.11 (source: evidence.json release.version; artifact frontmatter reports 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
