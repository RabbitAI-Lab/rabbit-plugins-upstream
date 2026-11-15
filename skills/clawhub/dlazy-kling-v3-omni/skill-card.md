## Description:

Generates videos with Kling v3 Omni from text prompts and multimodal references.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to generate videos from text prompts and image or video references, with options for duration, aspect ratio, mode, and sound.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local media supplied to the skill are sent to dLazy hosted services, and generated media URLs are hosted there.

Mitigation: Review prompts and media for sensitive content before sending them, and use the hosted service only when its data flow is acceptable.

Risk: The security review is partial and reports a purpose mismatch involving the login command.

Mitigation: Review the dLazy CLI and hosted service flow, and confirm the login and generation behavior match your intended use before running it.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/dlazyai/skills/dlazy-kling-v3-omni)
- [dLazy CLI repository (metadata link; release provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Generated media files, JSON, Shell commands, Configuration instructions]

**Output Format:** [Generated media delivered by URL with a JSON result envelope; command and configuration guidance is provided in Markdown.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generation may return an asynchronous task identifier; media URLs are hosted by dLazy.]

## Skill Version(s):

1.3.39 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
