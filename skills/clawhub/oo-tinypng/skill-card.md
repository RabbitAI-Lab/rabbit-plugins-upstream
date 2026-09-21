## Description:

This skill lets an agent compress images with TinyPNG and transform TinyPNG output images through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to compress images from public URLs or base64 image data and transform TinyPNG output images without directly handling TinyPNG API keys.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional installer commands can execute remote shell or PowerShell scripts.

Mitigation: Confirm trust in OOMOL and the oo CLI distribution source before following installer commands.

Risk: Write actions can create TinyPNG compressed image resources.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub TinyPNG skill page](https://clawhub.ai/oomol/skills/oo-tinypng)
- [TinyPNG homepage](https://tinypng.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns TinyPNG connector responses that may include transit URLs.]

## Skill Version(s):

1.0.4 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
