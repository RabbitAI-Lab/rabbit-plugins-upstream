## Description:

Turns a webpage URL into a promotional, social ad, or product demo video with the dLazy hosted agent.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers provide a webpage URL to create a promotional, social ad, or product demo video, and can continue work in a project session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review was partial and noted that some CLI steps were not clearly tied to the URL-to-video workflow.

Mitigation: Review the CLI installation and authentication guidance, and confirm commands fit the requested video task before running them.

Risk: The skill guide says prompts and optional attached files are sent to dLazy services.

Mitigation: Avoid sending sensitive prompts or files unless they are approved for processing by dLazy.

## Reference(s):

- [ClawHub release](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy homepage](https://dlazy.com)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Video, Text, Shell commands]

**Output Format:** [Rendered video with text status and guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video creation is managed through a dLazy project session.]

## Skill Version(s):

1.0.36 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
