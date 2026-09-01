## Description:

Generate and edit images with Nano Banana Pro, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to invoke dLazy's Nano Banana Pro image generation and editing service from an agent workflow, using prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced image files may be uploaded to dLazy services for processing.

Mitigation: Avoid sending sensitive content unless the deployment's data handling requirements permit use of the dLazy hosted API.

Risk: API usage may consume credits and can fail when the account has insufficient balance.

Mitigation: Use dry-run or review usage expectations before generation, and ensure the dLazy organization has available credits.

Risk: The skill depends on an external CLI and hosted API endpoints.

Mitigation: Review the pinned dLazy CLI source and install path before deployment when stronger supply-chain assurance is required.

Risk: An API key may be stored locally for repeated use.

Mitigation: Prefer least-privilege local access, rotate or revoke keys from the dLazy dashboard when needed, and use per-invocation environment variables where persistent storage is inappropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-banana-pro)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with CLI commands and JSON result objects.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images are returned as hosted URLs; the CLI can also save output assets to a local path.]

## Skill Version(s):

1.2.13 (source: server release metadata; artifact frontmatter reports 1.2.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
