## Description:

Guides an agent to create a same-length black-and-white human-segmentation mask video from a supplied video using the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to request human-segmentation masks for video compositing and matting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local media and request parameters are sent to dLazy services.

Mitigation: Review media and parameters before submission; do not upload sensitive content without authorization.

Risk: Installing and running the external dLazy CLI introduces package and credential exposure.

Mitigation: Review the pinned CLI package before installation, use the on-demand installation option if preferred, and use a revocable API key.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-videoseg)
- [dLazy CLI package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The CLI can return a media URL or an asynchronous task ID; the skill guides the agent in retrieving the result.]

## Skill Version(s):

1.3.29 (source: server-resolved ClawHub release; artifact frontmatter says 1.3.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
