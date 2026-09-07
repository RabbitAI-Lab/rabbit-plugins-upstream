## Description:

Generates detailed short-video storyboard scripts from user-provided themes, outlines, or structured copy while preserving spoken-script text verbatim.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, marketers, and video production teams use this skill to convert structured short-video copy or outlines into shot-by-shot storyboard scripts with scenes, camera movement, notes, and spoken script allocation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill presents itself as text-only storyboard writing but also contains guidance to install and run an image-generation CLI.

Mitigation: Install only when image-generation commands are expected, or request a cleaned text-only version with CLI install and execution guidance removed or separated.

Risk: Using the dLazy CLI may send prompts or referenced media to dLazy services and requires a dLazy account or API key.

Mitigation: Review prompts and media for sensitive content before use, and manage the API key through normal account controls such as rotation or revocation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI homepage](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, shell commands, configuration]

**Output Format:** [Markdown storyboard script with global video parameters and repeated shot sections]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to 9:16 and 720p when aspect ratio or resolution are not provided; spoken script text is expected to preserve the user's original copy verbatim.]

## Skill Version(s):

1.2.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
