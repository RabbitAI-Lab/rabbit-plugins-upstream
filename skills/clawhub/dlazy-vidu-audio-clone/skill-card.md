## Description:

Helps an agent clone an authorized voice from reference audio and generate speech reading new text through Vidu Audio Clone.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use the skill to generate spoken audio from text in the style of a reference voice they are permitted to clone.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference audio are sent to dLazy-hosted services.

Mitigation: Use the service only if you trust dLazy and are comfortable sharing the supplied content.

Risk: Voice cloning can be used without the speaker's permission.

Mitigation: Clone only voices you have permission to use.

Risk: The CLI stores an API key in the user's local configuration.

Mitigation: Protect the local config and review or rotate the API key if needed.

Risk: The sample result shows a PNG image despite the skill promising audio.

Mitigation: Check actual result types before treating an output URL as generated audio.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-vidu-audio-clone)
- [dLazy CLI project (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package (listed in skill metadata)](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance and shell commands; CLI results are JSON with hosted output URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Asynchronous calls may initially return a task ID instead of outputs; the artifact's sample mistakenly depicts PNG image output rather than audio.]

## Skill Version(s):

1.3.32 (source: ClawHub release metadata; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
