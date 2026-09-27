## Description:

Website to video, URL to video, landing page to video, link to ad, web promo video: capture the site, derive brand, storyboard, voiceover, build, and validate on a Remotion template when the user provides a URL and wants a promo, social ad, or product demo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to turn website URLs or landing pages into promotional videos, social ads, or product demos through the dLazy CLI and website-to-video template.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompt text, target URLs, project context, and attached files may be sent to dLazy as part of the hosted service workflow.

Mitigation: Use the skill only when this SaaS data flow is acceptable, and avoid attaching sensitive files unless they are intended for upload.

Risk: The dLazy CLI may store an API key in local configuration.

Mitigation: Use scoped organization keys, rotate or revoke keys from the dLazy dashboard when needed, and prefer per-invocation credentials where appropriate.

Risk: A global CLI install persists tooling on the system.

Mitigation: Use the documented npx invocation when a persistent global install is not desired.

## Reference(s):

- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and CLI guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May stream hosted dLazy agent responses and may reference generated project outputs or uploaded files.]

## Skill Version(s):

1.3.20 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
