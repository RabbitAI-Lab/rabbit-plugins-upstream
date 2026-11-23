## Description:

Creates reproducible screenshots and demo GIFs of command-line and terminal applications with Charm VHS.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gfargo](https://clawhub.ai/user/gfargo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to create repeatable terminal screenshots and short recordings for documentation, release materials, demos, or visual regression workflows. It also guides them in authoring VHS tapes and optimizing GIFs for web use.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary flags potential credential handling and sending repository content to an external service; scan coverage was partial.

Mitigation: Review the credential and external-service findings before installing. Keep real API keys and tokens out of tape files, and use synthetic or non-sensitive repository content unless the external transfer has been reviewed and approved.

## Reference(s):

- [Charm VHS](https://github.com/charmbracelet/vhs)
- [ClawHub release](https://clawhub.ai/gfargo/skills/vhs-cli-demos)
- [Server-resolved source](https://github.com/gfargo/skills/tree/main/plugins/terminal/skills/vhs-cli-demos)
- [VHS tape reference](references/tape-reference.md)
- [Recipe catalog pattern](references/recipe-catalog-pattern.md)

## Skill Output:

**Output Type(s):** [Guidance, Code, Shell commands, Files]

**Output Format:** [Markdown guidance, VHS tape files, shell commands, and captured PNG, GIF, or MP4 files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Capture results can be still images or motion recordings; GIFs can be optimized losslessly.]

## Skill Version(s):

0.1.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
