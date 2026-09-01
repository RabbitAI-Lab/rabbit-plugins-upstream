## Description:

Uses the dLazy CLI to submit PNG/JPG images to the dLazy hosted API for vectorization and return generated asset URLs or task status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, designers, and agents use this skill to convert logo, icon, and flat illustration image inputs into scalable vector-style assets through the dLazy CLI and hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local image paths passed to the CLI can result in uploads to dLazy-hosted endpoints.

Mitigation: Get explicit user confirmation before running the skill on local files, and avoid using sensitive or restricted images unless the upload is approved.

Risk: The evidence notes inconsistency about whether returned assets are guaranteed SVG.

Mitigation: Verify the returned MIME type and asset contents before treating the result as a vector SVG deliverable.

Risk: The skill depends on a third-party CLI package and hosted API.

Mitigation: Prefer the pinned npx invocation or a reviewed pinned install, and review the package/source links before persistent installation.

Risk: The skill requires a dLazy API key saved in local configuration or supplied through an environment variable.

Mitigation: Use organization-scoped keys, keep local config access restricted, and rotate or revoke keys when access changes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, JSON, Files]

**Output Format:** [Markdown guidance with bash commands and JSON result examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload local image inputs to dLazy-hosted endpoints and may return asynchronous task status when --no-wait is used.]

## Skill Version(s):

1.2.10 (source: server release evidence; artifact frontmatter reports 1.2.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
