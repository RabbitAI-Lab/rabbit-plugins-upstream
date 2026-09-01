## Description:

Convert static images into dynamic videos using the Vidu Q2 image-to-video model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to call dLazy's hosted Vidu Q2 image-to-video service from an agent workflow, supplying prompts and image inputs and receiving generated video results or async task identifiers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and local media inputs are sent to dLazy's hosted API and media storage.

Mitigation: Avoid passing private or sensitive media unless the user intends to upload it to the third-party service.

Risk: Saved CLI credentials can persist locally in the user's dLazy configuration file.

Mitigation: Use DLAZY_API_KEY for per-invocation credentials when less local persistence is preferred, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: The skill depends on a pinned third-party npm CLI and consumes service credits.

Mitigation: Review the pinned package and source before installation and confirm available account credits before running generation jobs.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-i2v)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated assets may be returned as hosted URLs or saved to a local path when requested.]

## Skill Version(s):

1.3.10 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
