## Description:

Generates high-quality text-to-video and image-to-video outputs through dLazy's hosted Kling v3 service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to ask an agent to generate videos from text prompts or up to two reference images using Kling v3 through the dLazy CLI and hosted API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and explicitly provided media files may be sent to dLazy's hosted service.

Mitigation: Use the skill only when cloud processing by dLazy is intended and the submitted content is appropriate for that service.

Risk: The dLazy CLI can save an API key in the local user configuration file.

Mitigation: Use DLAZY_API_KEY per run when avoiding persistent local credential storage, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Generated outputs are hosted by dLazy and returned as media URLs.

Mitigation: Treat generated URLs and downloaded assets according to the user's data handling requirements.

Risk: A global CLI install persists the pinned dLazy command on the system.

Mitigation: Use the pinned npx invocation when a per-run execution path is preferred.

## Reference(s):

- [dLazy CLI project](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with CLI commands and JSON service responses containing generated media URLs or async task identifiers.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets are returned as hosted URLs and may be downloaded locally with the CLI save option.]

## Skill Version(s):

1.3.18 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
