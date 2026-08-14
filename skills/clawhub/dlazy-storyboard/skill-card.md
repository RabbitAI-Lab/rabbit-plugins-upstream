## Description:

Storyboard converts prompts and references into multi-shot animated short video assets, including scripts, character and shot prompts, reference sheets, first and last frames, image-to-video shots, voice/TTS, music, sound effects, subtitles, and Remotion assembly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use this skill to run the dLazy storyboard template for project-scoped, multi-turn generation of animated short video components with consistent characters.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The dLazy API key may be stored in the local CLI configuration on shared or multi-user machines.

Mitigation: Use DLAZY_API_KEY per invocation or tighten permissions on ~/.dlazy/config.json; rotate or revoke the key if exposure is possible.

Risk: Files passed with --files are uploaded to dLazy media storage.

Mitigation: Attach only files intended for upload and avoid sending sensitive local files.

Risk: The reviewed CLI package does not enforce the user-only file permissions claimed by the skill documentation.

Mitigation: Review local configuration permissions after authentication and adjust them before use on shared systems.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-storyboard)
- [dLazy CLI homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May reference generated project assets, uploaded file URLs, and project IDs returned by the dLazy CLI.]

## Skill Version(s):

1.3.7 (source: server release metadata; artifact frontmatter reports 1.3.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
