## Description:

Generate cinematic videos from text prompts or images using Google Veo 3.1 through dLazy.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request text-to-video, image-guided video, and video extension through the dLazy CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media are sent to dLazy's cloud service.

Mitigation: Use the skill only when you are comfortable sharing those inputs with dLazy.

Risk: The dLazy CLI can persist an API key and a global installation.

Mitigation: Use the documented npx invocation if you prefer no persistent global binary, and rotate or revoke the saved key when you stop using the service.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-veo-3-1)
- [dLazy CLI source (declared in skill metadata)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON responses, Video links, Guidance]

**Output Format:** [CLI guidance and JSON results with generated media URLs or asynchronous task status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save generated media locally when requested.]

## Skill Version(s):

1.3.25 (source: ClawHub release metadata; artifact frontmatter states 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
