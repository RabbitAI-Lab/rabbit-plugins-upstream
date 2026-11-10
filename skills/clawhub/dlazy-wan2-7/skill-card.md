## Description:

Generates Tongyi Wanxiang 2.7 videos from text prompts, reference media, or first and last frames.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

People creating short videos can use text prompts, reference images or videos, or first and last frames to request generated video through the dLazy service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment reports a possible mismatch involving the login command and notes partial analysis coverage.

Mitigation: Review the setup details and CLI login flow before authenticating, and confirm that the sign-in step is expected for your use.

Risk: The skill documents that prompts and supplied local media are sent to dLazy hosted services for generation.

Mitigation: Only submit prompts and media that are appropriate for processing by the hosted service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-wan2-7)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)
- [CLI repository listed in artifact metadata](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [Video, JSON, Shell commands, Configuration instructions]

**Output Format:** [Generated media URL and task status in a JSON CLI response; command and setup guidance in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation accepts a prompt and optional media or frame inputs, with resolution, duration, and wait or save options.]

## Skill Version(s):

1.3.37 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
