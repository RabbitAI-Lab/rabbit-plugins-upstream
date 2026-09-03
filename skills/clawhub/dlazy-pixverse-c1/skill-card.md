## Description:

PixVerse C1 generates videos from text, images, first and last frames, or reference images, with strengths in action, VFX, and high-motion scenes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate short PixVerse C1 videos through the dLazy CLI, including text-to-video, image-to-video, first/last-frame, and reference-image workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and media files passed to the skill are sent to dLazy cloud endpoints for generation.

Mitigation: Confirm dLazy/PixVerse C1 is the intended service before use and avoid sending sensitive media unless that cloud processing is acceptable.

Risk: Using dlazy login stores an API key in the local dLazy configuration.

Mitigation: Use DLAZY_API_KEY per command or npx @dlazy/cli@1.2.3 for less persistence, and rotate or revoke keys from the dLazy dashboard when needed.

Risk: Broad trigger terms such as video generation may route requests to this skill unintentionally.

Mitigation: Confirm the user wants PixVerse C1 before invoking dlazy pixverse-c1.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-pixverse-c1)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, JSON, Files]

**Output Format:** [Markdown guidance with inline bash commands and JSON responses from the dLazy CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted generated asset URLs, asynchronous task identifiers, or optionally save generated assets to a local path.]

## Skill Version(s):

1.2.12 (source: server release metadata; artifact frontmatter reports 1.2.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
