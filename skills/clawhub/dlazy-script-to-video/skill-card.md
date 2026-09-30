## Description:

Helps turn scripts into storyboarded video projects through dLazy, although the bundled skill files contain conflicting MiniMax H3 instructions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and developers use dLazy to plan shots and produce video from a script or scene breakdown; confirm the intended workflow before running this release.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled files disagree about the skill name, version, and video workflow.

Mitigation: Confirm the intended release and command before installing or running the skill.

Risk: Prompts and explicitly attached files are sent to dLazy's service.

Mitigation: Review prompts and file contents before sending; attach only files intended for upload.

Risk: Using the skill requires running the dLazy CLI and authenticating with an API key.

Mitigation: Review the pinned npm package before installation and rotate or revoke the key if needed.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-script-to-video)
- [dLazy CLI source (linked in skill metadata; not verified release provenance)](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Text guidance and CLI responses with generated media links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video projects and media are handled by the dLazy service.]

## Skill Version(s):

1.0.20 (source: ClawHub release metadata; bundled frontmatter disagrees)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
