## Description:

Fast response and generation of short videos with Google Veo 3.1 Fast, supporting text-to-video and image-to-video workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate or extend short videos through the dLazy hosted Google Veo 3.1 Fast wrapper from text prompts and optional image or video inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image or video files are sent to dLazy-hosted API and media storage endpoints.

Mitigation: Confirm the user is comfortable sending the selected content to dLazy before use, and avoid submitting sensitive material unless permitted.

Risk: Authentication stores a dLazy organization API key in local CLI configuration.

Mitigation: Prefer one-off npx execution when avoiding a global install, protect shared machines, and rotate or revoke the API key if the machine is shared or compromised.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1-fast)
- [dLazy CLI homepage and source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result objects]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted media URLs, asynchronous task identifiers, or saved local video assets depending on CLI options.]

## Skill Version(s):

1.3.10 (source: server release evidence; artifact frontmatter reports 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
