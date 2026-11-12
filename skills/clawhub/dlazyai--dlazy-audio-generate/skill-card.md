## Description:

Automatically selects a dLazy CLI audio or text-to-speech model based on the user's prompt.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to turn prompts into speech, dialogue, music, or sound effects by selecting an appropriate dLazy CLI audio model. It requires a dLazy API key and can pass generated media between CLI commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence reports a benign result with medium confidence, but notes an audio-purpose mismatch: the reported pipelines also generate images and video and upscale images. The scan was partial.

Mitigation: Review the install details and skill behavior before installation, and treat the scan result as limited rather than a safety guarantee.

Risk: Prompts and any local media supplied to the CLI are sent to dLazy hosted services; API credentials are also required.

Mitigation: Only submit prompts and media you are comfortable sending to the service, and authenticate through the documented CLI login or a protected environment variable.

## Reference(s):

- [dLazy CLI source repository (listed in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-audio-generate)

## Skill Output:

**Output Type(s):** [Audio files, Text, Shell commands, Configuration instructions]

**Output Format:** [Generated audio media and CLI JSON result envelopes, with command and setup guidance in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audio outputs are returned as hosted URLs; CLI results can be piped into later commands.]

## Skill Version(s):

1.3.43 (source: server-resolved release; artifact frontmatter lists 1.3.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
