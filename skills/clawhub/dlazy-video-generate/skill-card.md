## Description:

Video generation skill that selects an appropriate dLazy CLI video model for text-to-video, image-to-video, image animation, first/last-frame video, digital human, and lip-sync requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, developers, and agents use this skill to choose and run dLazy video-generation commands for prompts, source images, source video, audio, digital-human generation, and lip-sync workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and selected image, video, or audio files may be sent to dLazy's cloud service.

Mitigation: Use the skill only for media and prompts approved for dLazy cloud processing.

Risk: The dLazy API key may be saved in the local CLI configuration.

Mitigation: On shared or managed machines, prefer the DLAZY_API_KEY environment variable for per-run authentication instead of saving the key locally.

Risk: Generated outputs are hosted remotely and API use may consume credits.

Mitigation: Review generated output URLs and account credit use according to the user's dLazy organization policies.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-video-generate)
- [dLazy homepage](https://dlazy.com)
- [dLazy CLI source link from metadata](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline bash commands and JSON CLI output envelopes.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return remote media URLs hosted by dLazy after execution.]

## Skill Version(s):

1.4.13 (source: server release evidence; artifact frontmatter reports 1.4.6)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
