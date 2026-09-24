## Description:

A structured skill for multi-platform social-media content creation, covering Instagram, TikTok, YouTube, LinkedIn, Xiaohongshu, and other formats with platform-specific layout, copy, safe-area, and generation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to plan and generate social-media visuals and accompanying captions for platform-specific posts, carousels, stories, shorts, thumbnails, and professional content.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media file paths supplied for generation may be sent to dLazy-hosted endpoints.

Mitigation: Avoid submitting confidential, sensitive, or unapproved media, and review dLazy's service expectations before using hosted generation.

Risk: Authentication stores a dLazy API key in the user's local CLI configuration.

Mitigation: Use an organization-scoped key, rotate or revoke it when needed, and prefer per-command environment variables when persistent local credentials are not desired.

Risk: Global CLI installation creates a long-lived dependency on the local machine.

Mitigation: Use the documented npx command for ad hoc execution when a persistent global install is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-image-social-media)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with structured planning, copy, checks, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted image result URLs from the dLazy service after CLI execution.]

## Skill Version(s):

1.3.21 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
