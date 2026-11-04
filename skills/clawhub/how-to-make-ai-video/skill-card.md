## Description:

Helps agents find and plan AI video workflows by matching a request to relevant skills, presenting options, and outlining next steps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents helping creators or teams choose how to make an AI video use this skill to find a suitable format skill, compare options, share its install command, and outline production steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Personalized searches use an existing Varg credential, and search requests go to Varg.

Mitigation: Use anonymous search if you do not want account use.

Risk: The workflow may install downloaded skills and use paid services during full productions.

Mitigation: Review downloaded skills and installation commands before running them; confirm the repository and agree a spend cap before a full production.

## Reference(s):

- [Varg how-to](https://varg.ai/how-to)
- [ClawHub release page](https://clawhub.ai/vargai/skills/how-to-make-ai-video)
- [Whole video prompt](references/whole-video-prompt.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown guidance with links, options, install commands, and production steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Recommendations depend on the video request; a full-production workflow includes review stops and budget checks.]

## Skill Version(s):

1.0.14 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
