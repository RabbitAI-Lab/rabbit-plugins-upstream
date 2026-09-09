## Description:

Generate high-quality images with Doubao Seedream 4.5 for text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content teams use this skill to call dLazy's Seedream 4.5 image-generation workflow from an agent, providing prompts and optional source images and receiving generated image outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media are sent to dLazy's hosted API and media storage.

Mitigation: Use only prompts and media approved for third-party SaaS processing, and review dLazy service terms before use.

Risk: Authentication can store a dLazy API key in the local CLI config.

Mitigation: Protect the local config, prefer per-invocation environment credentials when appropriate, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on installing or invoking a third-party npm CLI.

Mitigation: Prefer the pinned on-demand npx path when avoiding a global install, and review the package/source before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedream-4-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI guidance and JSON results containing generated image URLs, with optional saved image files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async mode can return a generation task identifier for later polling.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
