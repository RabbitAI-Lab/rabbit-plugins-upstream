## Description:

Turns a webpage URL into a promotional, social-ad, or product-demo video using dLazy's hosted service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and developers can provide a webpage URL to make a promotional video, social ad, or product demo and refine it through follow-up requests.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing and running an external CLI package introduces third-party software into the workflow.

Mitigation: Review the pinned @dlazy/cli@1.2.3 package before installing it.

Risk: Prompts, URL or task details, and attached files are sent to dLazy's hosted service.

Mitigation: Avoid sending sensitive material without authorization; use DLAZY_API_KEY for per-run authentication if you do not want the key saved in local configuration.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-url-to-video)
- [dLazy CLI repository (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Text and CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The agent guides video creation through a hosted service; video generation is not itself a text output.]

## Skill Version(s):

1.0.22 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
