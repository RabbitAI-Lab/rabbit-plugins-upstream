## Description:

Uses Kimi K3 through the dLazy CLI for complex analysis, coding, writing, and image or video understanding.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can ask Kimi K3 for analysis, code, and writing, with optional images or videos as input.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image or video files may be sent to the dLazy service.

Mitigation: Review content and local file paths before sending sensitive material.

Risk: Logging in stores a service API key locally.

Mitigation: Use DLAZY_API_KEY per invocation when persistent credential storage is unsuitable.

Risk: The skill depends on a third-party CLI package and cloud API.

Mitigation: Confirm you trust the dLazy package and service before installing or invoking them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-kimi-k3)
- [dLazy CLI repository (linked in skill metadata; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance]

**Output Format:** [Text or structured JSON response from the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous requests can return a task identifier for later retrieval.]

## Skill Version(s):

1.2.26 (source: ClawHub release metadata; skill frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
