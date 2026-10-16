## Description:

Helps agents generate videos from text or images, or extend video, using Veo 3.1 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to instruct an agent to generate short videos from prompts and reference images or extend existing footage through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing the external dLazy CLI runs third-party code.

Mitigation: Review the pinned @dlazy/cli package and its source before installing.

Risk: Prompts and supplied media are sent to dLazy for cloud processing.

Mitigation: Use only prompts and media that you are willing to share with dLazy.

Risk: The CLI can store a long-lived API key in local configuration.

Mitigation: Use DLAZY_API_KEY for per-run authentication if persistent key storage does not fit your security model.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI source (skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (skill metadata)](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Configuration instructions]

**Output Format:** [Markdown with shell commands and JSON result details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned by the service as a URL and can optionally be saved locally.]

## Skill Version(s):

1.3.29 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
