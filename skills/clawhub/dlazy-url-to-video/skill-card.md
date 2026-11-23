## Description:

URL to Video turns a webpage into a promotional, social ad, or product demo video by capturing the page, deriving its brand, and building a storyboard and video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, marketers, and product teams can provide a webpage URL and use the dLazy hosted agent to create a promotional video, social ad, or product demo, then continue work in a project session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan was partial and flagged project-listing and login behavior for review.

Mitigation: Review the CLI install instructions and unresolved references before installing.

Risk: Messages are sent to the dLazy API, and files attached with --files are uploaded to its media storage.

Mitigation: Avoid sending sensitive messages or files unless they are appropriate to share with the hosted service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy CLI source and documentation link](https://github.com/dlazy-ai/cli)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Video, Text, Guidance]

**Output Format:** [Video project assets and text responses through the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-based sessions; output depends on the webpage and user prompt.]

## Skill Version(s):

1.0.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
