## Description:

Creates promo, social ad, or product demo videos from a website URL by capturing the site, deriving brand context, storyboarding, adding voiceover, building, and validating on a Remotion template.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, content teams, and marketing teams use this skill to turn a supplied website URL into a promotional, social advertising, or product demo video through the dLazy hosted website-to-video workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, website URLs, and explicitly attached files are sent to dLazy API and media storage.

Mitigation: Use the skill only with data approved for third-party processing, and avoid sensitive client material unless your organization has approved the service.

Risk: The dLazy API key may be stored in local CLI configuration, and the security evidence questions how strongly local permission restrictions are enforced.

Mitigation: Prefer per-invocation DLAZY_API_KEY or npx on shared machines, restrict local account access, and rotate or revoke the key if local access controls are uncertain.

Risk: A global CLI install persists the dLazy command on the local system.

Mitigation: Review the pinned package before installing and use the documented npx invocation when a temporary execution path is more appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-website-to-video)
- [dLazy CLI source](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Files, Guidance]

**Output Format:** [Markdown and terminal text; the hosted service may return project status, links, or generated video assets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx and a dLazy API key; prompts, URLs, and explicitly attached files are sent to dLazy services.]

## Skill Version(s):

1.3.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
