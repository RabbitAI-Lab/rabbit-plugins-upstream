## Description:

Helps agents choose a dLazy video model and generate videos from text, images, reference frames, or audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to direct an agent to generate or adapt videos, including text-to-video, image-to-video, and lip-synced clips through dLazy.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and supplied media are sent to dLazy services for generation.

Mitigation: Use the service only if its cloud processing is acceptable for the content; avoid submitting sensitive media or prompts.

Risk: The dLazy CLI uses a stored API key to access the service.

Mitigation: Treat the key as a credential and rotate or revoke it if no longer trusted.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy CLI repository (listed in skill metadata; import provenance unavailable)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance]

**Output Format:** [Text with inline shell commands and links to generated videos]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video results are returned as hosted URLs by the dLazy service.]

## Skill Version(s):

1.4.31 (source: ClawHub release metadata; bundled skill frontmatter says 1.4.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
