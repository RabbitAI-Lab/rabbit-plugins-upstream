## Description:

Convert static images into dynamic videos using the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to invoke dLazy's Vidu Q2 image-to-video workflow from an agent, passing prompts and image inputs to generate short videos.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected media files, prompts, parameters, and the API key are sent to dLazy's hosted service.

Mitigation: Install only if you trust dLazy, avoid private media unless upload is intended, and rotate or revoke the API key from the dLazy dashboard when needed.

Risk: The skill depends on the dLazy CLI package and external endpoints for execution and generated result hosting.

Mitigation: Use the pinned CLI version from the skill metadata, prefer npx when a global install is not desired, and review the linked CLI source before installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, API Calls, Files]

**Output Format:** [JSON responses with generated media URLs and optional downloaded result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs, polling, local save paths, dry runs, and cloud-hosted result URLs.]

## Skill Version(s):

1.3.13 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
