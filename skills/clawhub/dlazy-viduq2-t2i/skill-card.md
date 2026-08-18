## Description:

Generate high-quality images with Vidu Q2 through dLazy's hosted API, supporting text-to-image and image-to-image workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creative users invoke this skill to generate or edit images with Vidu Q2 from prompts and optional reference images through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and image inputs may be uploaded to dLazy's hosted service.

Mitigation: Use the skill only with content approved for dLazy cloud processing and avoid passing sensitive local files unless that use is authorized.

Risk: API keys can be saved in the local dLazy CLI configuration.

Mitigation: Use per-invocation DLAZY_API_KEY when appropriate, and rotate or revoke saved keys from the dLazy dashboard if access changes.

Risk: Generated files are hosted by dLazy and API calls may consume account credits.

Mitigation: Review generated output URLs and account credit usage, and use dry-run or asynchronous polling options when they fit the workflow.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-viduq2-t2i)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, API calls, Files, Guidance]

**Output Format:** [CLI commands and JSON responses with generated image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return a generated image URL or an asynchronous generateId for polling.]

## Skill Version(s):

1.3.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
