## Description:

Text-to-image generation with Jimeng, quickly converting text to high-quality images.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate Jimeng text-to-image outputs from prompts and optional reference images through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and explicitly referenced local media files to dLazy's hosted service.

Mitigation: Use it only with content approved for dLazy processing, and avoid passing sensitive local files unless the user has explicitly consented.

Risk: The skill requires a dLazy API key that may be stored in the local CLI configuration.

Mitigation: Protect the local configuration file, prefer per-invocation credentials when appropriate, and rotate or revoke keys from the dLazy dashboard if exposure is suspected.

Risk: Installing the global dLazy CLI creates persistent tooling on the host.

Mitigation: Use the pinned npx/on-demand command path when a persistent global install is not desired.

Risk: Image-generation requests can consume account credits.

Mitigation: Use dry-run or explicit confirmation for broad generation requests before making paid API calls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-jimeng-t2i)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Files]

**Output Format:** [JSON response with generated image URLs; optional saved image file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a dLazy API key and may return asynchronous task identifiers when no-wait mode is used.]

## Skill Version(s):

1.3.16 (source: server release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
