## Description:

通义万相 Wan 2.7 video generation skill for text-to-video, first/last-frame-to-video, and reference-to-video through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate Wan 2.7 videos from prompts, reference images or videos, first and last frames, and optional audio through dLazy's hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill installs or runs an external dLazy npm CLI and uses dLazy's hosted cloud service.

Mitigation: Install only if comfortable with that external dependency; prefer the pinned npx invocation to avoid keeping a persistent global binary.

Risk: Prompts and media paths supplied to the CLI can be uploaded to dLazy API and file endpoints for generation.

Mitigation: Avoid submitting sensitive prompts or media unless sharing them with dLazy is acceptable for the intended use case.

Risk: Login can store a dLazy API key in the local CLI configuration.

Mitigation: Protect the local config file, use per-invocation DLAZY_API_KEY when preferred, and rotate or revoke keys from the dLazy dashboard when needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI commands and JSON responses containing generated media URLs; optional downloaded media file when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to dLazy API and file endpoints.]

## Skill Version(s):

1.3.18 (source: release metadata; artifact frontmatter: 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
