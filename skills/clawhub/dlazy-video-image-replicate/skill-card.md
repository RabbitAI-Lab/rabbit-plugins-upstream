## Description:

Studies a user-provided reference image or video, then helps recreate the same look and structure with the user's own subject, product, or characters.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to recreate the style, composition, and structure of a reference image or video with their own content through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Referenced images, videos, prompts, and attached files may be sent to dLazy services.

Mitigation: Avoid uploading private, regulated, or sensitive media unless the user has approved using dLazy as an external service.

Risk: API keys may be persisted in the local dLazy CLI configuration.

Mitigation: Prefer per-invocation credentials or a protected config location when possible, and rotate or revoke organization keys after use when appropriate.

Risk: Continuing an existing project may reuse prior session context.

Mitigation: Review the selected project before continuing and use clear/logout controls when the previous context should not carry forward.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-video-image-replicate)
- [dLazy CLI Source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or terminal text with inline shell commands and service-returned media references.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference uploaded media, generated assets, and project-scoped session context returned by dLazy.]

## Skill Version(s):

1.3.12 (source: server release metadata; artifact frontmatter says 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
