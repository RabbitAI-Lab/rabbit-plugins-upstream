## Description:

Generates detailed short-video storyboard scripts from user-provided themes, structured copy, or outlines while preserving spoken script text word for word.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and content creators use this skill to transform themes, outlines, or structured marketing copy into shot-by-shot storyboard scripts for short videos. It defines video parameters, scene descriptions, camera movement, notes, shooting technique, and spoken script allocation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The release security summary says the skill is presented as text-only storyboard writing but also instructs use of a third-party media-generation CLI with API-key storage and network uploads.

Mitigation: Use it only when dLazy CLI-based media generation is intended, review the skill before execution, and avoid sending sensitive prompts or media inputs to the dLazy services.

Risk: The artifact describes storing a dLazy API key in a local CLI configuration file.

Mitigation: Prefer the DLAZY_API_KEY environment variable when practical, protect local configuration files, and rotate or revoke keys if exposure is suspected.

Risk: The release security guidance warns that prompts and selected media inputs may go to dLazy services.

Mitigation: Confirm that organizational policy permits use of api.dlazy.com and files.dlazy.com before using confidential, regulated, or customer-provided material.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/dlazyai/skills/dlazy-text-storyboard-script)
- [dLazy CLI Homepage](https://github.com/dlazyai/cli)
- [dLazy CLI npm Package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy Website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown storyboard script with structured shot sections and optional inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes global video parameters, per-shot scene and camera guidance, and spoken script text preserved from user input.]

## Skill Version(s):

1.2.7 (source: server release evidence; artifact frontmatter lists 1.2.3)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
