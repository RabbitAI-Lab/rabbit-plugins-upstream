## Description:

Generates and edits images from text prompts or reference images with Nano Banana 2.0 via the dLazy service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use this skill to request new images or edit images using text prompts and optional reference images.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and reference images may be uploaded to a third-party cloud service.

Mitigation: Avoid submitting sensitive content without reviewing the service and its terms.

Risk: Image requests may consume API credits.

Mitigation: Check estimated costs before making paid requests.

Risk: The CLI can store a dLazy API key on the local machine.

Mitigation: Protect local credentials and review the third-party CLI before installing it.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/dlazyai/skills/dlazy-banana2)
- [dLazy CLI source (linked in skill metadata; not verified import provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Shell commands, Guidance, Image URLs]

**Output Format:** [Markdown guidance and shell commands; CLI results include JSON image URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images can be saved locally when requested.]

## Skill Version(s):

1.3.22 (source: server release evidence; artifact frontmatter lists 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
