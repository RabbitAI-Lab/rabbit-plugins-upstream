## Description:

Generates videos through the dLazy Seedance 2.0 CLI using text prompts and optional image, video, audio, or first/last-frame references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, creators, and agents use this skill to invoke dLazy's Seedance 2.0 video-generation CLI for text-to-video, first/last-frame, and multimodal reference workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or running the skill executes third-party dLazy CLI code through npm or npx.

Mitigation: Prefer the pinned npx invocation or an isolated environment, and review the package/source before installing globally.

Risk: A global install persists a CLI binary on the user's system.

Mitigation: Use the on-demand npx path when persistence is not needed, or uninstall the global package after use.

Risk: dLazy login stores an API key in the local CLI configuration.

Mitigation: Use a revocable API key, keep the config file user-restricted, and rotate or revoke the key if it is no longer needed.

Risk: Prompts and selected image, video, or audio files are uploaded to dLazy services for generation.

Mitigation: Only provide prompts and files intended for upload to dLazy, and avoid sensitive media unless the service terms and data handling are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI command guidance plus JSON result payloads with generated media URLs; optional saved media files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key. Local media inputs may be uploaded to dLazy, and asynchronous mode can return a task identifier for polling.]

## Skill Version(s):

1.3.13 (source: release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
