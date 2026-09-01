## Description:

A comprehensive generation skill that helps agents generate images, videos, and audio by selecting and invoking the appropriate dLazy CLI model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to route natural-language media-generation requests to dLazy CLI commands for image, video, audio, speech, music, and related media-processing outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and uploaded media files are sent to dLazy services and generated results are hosted by dLazy.

Mitigation: Use the skill only for content you are comfortable sending to dLazy, and avoid passing sensitive local files.

Risk: The skill encourages saved API-key authentication for a remote paid service.

Mitigation: Prefer per-run DLAZY_API_KEY use when persistent local credentials are not desired, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Broad generation triggers could cause unintended remote API use or paid credit consumption.

Mitigation: Invoke the skill only when the user specifically intends to use dLazy media generation and accepts any associated credit usage.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-generate)
- [Publisher Profile](https://clawhub.ai/user/dlazyai)
- [dLazy CLI Homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, JSON]

**Output Format:** [Markdown guidance with inline shell commands and JSON result envelopes from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated media is returned as hosted URLs from dLazy services.]

## Skill Version(s):

1.3.9 (source: server release evidence; artifact frontmatter says 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
