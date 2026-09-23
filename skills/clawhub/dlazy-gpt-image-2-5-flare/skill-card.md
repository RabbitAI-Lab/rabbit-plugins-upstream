## Description:

GPT Image 2.5 Flare, the speed tier of OpenAI's GPT Image 2.5 series, supports text-to-image generation and image editing with reference images, aspect ratios up to 21:9, and quality up to max.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke the dLazy CLI for GPT Image 2.5 Flare image generation and editing workflows, including prompt-only generation and reference-image based edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference files are sent to the dLazy API, and generated files are hosted by dLazy.

Mitigation: Review data sensitivity before use and avoid submitting confidential or restricted files unless the user's organization approves that SaaS workflow.

Risk: Authentication requires a dLazy API key that may be stored in the local CLI configuration or supplied through an environment variable.

Mitigation: Use organization-approved secret handling, restrict local config access, and rotate or revoke the key from the dLazy dashboard if exposure is suspected.

Risk: The workflow uses a third-party npm CLI that can be installed globally.

Mitigation: Review the package/source before installation and use the pinned npx invocation when avoiding a persistent global CLI install.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2-5-flare)
- [dLazy CLI Repository](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Images, JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with generated image URLs, optional saved image files, and Markdown command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports asynchronous task IDs when --no-wait is used; generated assets are hosted by dLazy.]

## Skill Version(s):

1.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
