## Description:

Generate and edit images with Nano Banana Pro for text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate or edit images through the dLazy Nano Banana Pro CLI, including text-to-image and image-to-image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local image paths provided to the CLI are sent to dLazy services for generation.

Mitigation: Avoid sending sensitive prompts or media unless the user intends to share them with dLazy, and review dLazy service terms before use.

Risk: Generated result URLs are hosted by dLazy media storage.

Mitigation: Treat generated URLs as externally hosted assets, download needed files deliberately, and manage retention or sharing outside the skill.

Risk: The CLI requires a dLazy API key that may be stored in local configuration.

Mitigation: Keep the key scoped to the intended organization, use per-run environment variables when appropriate, and rotate or revoke keys that are no longer needed.

Risk: A global npm install persists a third-party CLI on the user's machine.

Mitigation: Prefer pinned per-run npx usage or review the local install and source package before using a persistent global install.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [CLI commands and JSON responses containing generated image URLs, with optional downloaded image files when --save is used.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Async runs can return a generateId and task status for later polling.]

## Skill Version(s):

1.2.16 (source: server release metadata; artifact frontmatter reports 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
