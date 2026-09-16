## Description:

Image-to-SVG tool: converts raster images (PNG/JPG) into color vector SVG and returns a URL for vectorization workflows involving logos, icons, and flat illustrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent invoke dLazy's CLI for raster image vectorization and return generated result URLs. It is suited to logo, icon, and flat illustration conversion workflows where selected images can be sent to the dLazy hosted service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an external npm CLI and offers a global install path.

Mitigation: Review the package before use and prefer npx or a local install over a global install when possible.

Risk: Selected images and prompts are sent to dLazy API and media storage endpoints.

Mitigation: Use the skill only for images and prompts that are acceptable to send to dLazy and review the service terms before deployment.

Risk: The dLazy API key may be stored in a local CLI configuration file.

Mitigation: Restrict local config access, consider per-invocation DLAZY_API_KEY use for sensitive environments, and rotate or revoke keys when needed.

Risk: The SVG-oriented description conflicts with PNG-style output examples.

Mitigation: Confirm the returned MIME type and asset contents before relying on the output as vector SVG.

Risk: Authentication retries or insufficient-balance handling could cause unwanted account or credit actions.

Mitigation: Require user confirmation before retrying authentication, recharging, or spending additional credits.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-vectorize)
- [dLazy Homepage](https://dlazy.com)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON result URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted files.dlazy.com URLs, async task identifiers, or saved local assets when the CLI save option is used.]

## Skill Version(s):

1.2.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
