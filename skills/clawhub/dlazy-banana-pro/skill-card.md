## Description:

Generate and edit images with Nano Banana Pro using text-to-image and image-to-image prompts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to generate or edit images through the dLazy Nano Banana Pro CLI, including prompts with optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected media files can be uploaded to dLazy cloud services for generation or editing.

Mitigation: Only submit prompts and media the user intends to share with dLazy, and avoid confidential or sensitive inputs unless the user's policy allows it.

Risk: Generated outputs are hosted by dLazy and may be returned as remote file URLs.

Mitigation: Handle generated URLs and downloaded assets according to the user's data handling requirements.

Risk: The dLazy CLI may store an API key in the local user configuration.

Mitigation: Use per-invocation environment variables or npx when less persistence is desired, and rotate or revoke API keys from the dLazy dashboard when needed.

Risk: Using the skill requires running a third-party npm or npx CLI.

Mitigation: Install only if comfortable using dLazy as a third-party cloud service and prefer the pinned command from the release metadata.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON result payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted image URLs, download generated assets with --save, or return an asynchronous task identifier when --no-wait is used.]

## Skill Version(s):

1.2.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
