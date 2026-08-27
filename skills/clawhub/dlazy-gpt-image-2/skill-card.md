## Description:

GPT Image 2 generates images from text and edits or synthesizes images using reference inputs through the dLazy CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to have an agent generate, edit, and synthesize images with GPT Image 2 using prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, parameters, and selected local media files are sent to dLazy cloud APIs for generation.

Mitigation: Review prompts and referenced media before invocation, and avoid sending sensitive or unapproved content.

Risk: The dLazy API key may be stored in the local dLazy configuration file for persistent login.

Mitigation: Protect the local configuration file, prefer per-invocation environment variables when appropriate, and rotate or revoke exposed keys.

Risk: Generated image outputs are returned as externally hosted URLs on dLazy file storage.

Mitigation: Review sharing, retention, and distribution requirements before using or publishing generated output URLs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-gpt-image-2)
- [dLazy CLI Source](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance, JSON]

**Output Format:** [Markdown guidance with bash command examples and JSON CLI result examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI results include generated image metadata, hosted output URLs, and optional saved image files.]

## Skill Version(s):

1.3.9 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
