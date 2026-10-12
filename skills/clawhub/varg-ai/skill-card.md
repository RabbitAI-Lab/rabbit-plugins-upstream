## Description:

Helps agents generate videos, images, speech, and music with varg through cloud or local rendering workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[securityqq](https://clawhub.ai/user/securityqq)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to plan and generate media assets or composed videos, using the varg cloud API or local rendering tools.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, rendering code, asset URLs, and authenticated jobs are sent to varg.ai during cloud workflows.

Mitigation: Use the service only when sharing that content with varg.ai is acceptable.

Risk: Credential setup may persist the API key in a local credentials file or append it to a project .env file.

Mitigation: Prefer a session-scoped environment variable or OS secret store; only write project secrets to a gitignored file.

Risk: The skill suggests a self-update command that may replace installed skill content.

Mitigation: Review the update and its source before running it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/securityqq/skills/varg-ai)
- [varg homepage](https://varg.ai)
- [Cloud rendering guide](references/cloud-render.md)
- [Local rendering guide](references/local-render.md)
- [Gateway API reference](references/gateway-api.md)
- [Model selection guide](references/models.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Configuration instructions]

**Output Format:** [Markdown with code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media generation requires an API key and may incur usage charges; local rendering also requires bun and ffmpeg.]

## Skill Version(s):

2.0.10 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
