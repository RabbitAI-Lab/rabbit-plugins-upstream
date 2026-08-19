## Description:

Generates 1MP raster images with refined design judgment for everyday creative work and fast iteration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and creative developers use this skill to request Recraft V4 image generations through the dLazy CLI, choosing prompts and aspect ratios for fast creative iteration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can persist a dLazy API key in a local CLI configuration file.

Mitigation: Prefer per-invocation DLAZY_API_KEY for sensitive environments, or manually verify restrictive permissions on ~/.dlazy/config.json and rotate or revoke keys when needed.

Risk: Prompts and local files passed to media fields are sent to dLazy hosted API and storage endpoints.

Mitigation: Only submit prompts and files that are appropriate to upload to the dLazy hosted service.

Risk: The security summary flags the referenced third-party CLI because claimed restricted config-file permissions may not be enforced.

Mitigation: Review the skill and CLI before installation, and use the pinned npx invocation when avoiding a persistent global install is preferred.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-recraft-v4)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [JSON, image URL, shell commands, configuration guidance]

**Output Format:** [JSON response with generated image metadata and hosted output URLs; Markdown documentation includes shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports synchronous waits, async generation IDs, dry-run cost estimates, prompt input, and aspect ratio selection.]

## Skill Version(s):

1.3.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
