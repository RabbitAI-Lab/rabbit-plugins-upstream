## Description:

视频生成 Seedance 2.0 helps agents use dLazy's Seedance 2.0 CLI wrapper to generate videos from prompts and optional image, video, audio, or first/last-frame references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short videos through dLazy's hosted Seedance 2.0 service, using text prompts plus optional media references and output-saving options.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image, video, or audio files are sent to dLazy cloud endpoints for generation.

Mitigation: Use the skill only with content acceptable for dLazy processing and avoid sensitive media unless the user's data-handling requirements allow it.

Risk: The dLazy CLI stores or uses an API key for authenticated requests.

Mitigation: Prefer per-invocation environment variables when persistence is not desired, protect ~/.dlazy/config.json, and rotate or revoke the key when access is no longer needed.

Risk: Installing the pinned npm CLI introduces normal package and persistent-binary trust considerations.

Mitigation: Use the pinned npx command for on-demand execution when a global install is unnecessary and review the linked package/source before installing.

Risk: Video generation may consume dLazy credits.

Mitigation: Use dry-run or cost-estimation behavior when appropriate and confirm available credits before long or repeated generations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [dLazy API key dashboard](https://dlazy.com/dashboard/organization/api-key)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown instructions with CLI commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated media URLs, async task IDs, or save downloaded assets to a local path.]

## Skill Version(s):

1.3.14 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
