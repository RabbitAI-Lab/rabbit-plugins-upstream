## Description:

Turns recorded talking-head footage into a publishable cut by reorganizing only spoken content, cleaning speech, adding captions, and optionally planning B-roll.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

Video creators use this skill to assemble Chinese talking-head recordings into an editable cut, with content restructuring, speech cleanup, captions, and optional approved B-roll. If the editing tool is unavailable, it can provide a timestamped edit plan from local transcription.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow may access video projects, transcripts, vault rules, and scoped memory.

Mitigation: Confirm access to those materials is appropriate before installing or using the skill.

Risk: Account-specific editing defaults may be inappropriate for another creator.

Mitigation: Use the named account's defaults only after confirming the account or finding a matching configuration.

Risk: Generated footage and paid editing actions may incur costs or misrepresent real events.

Mitigation: Review and approve paid actions before submission; do not use generated footage as evidence of real events, and disclose AI-generated media when publishing.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/iamzifei/skills/aikey-cut)
- [ChatCut editing and verification](artifact/references/ChatCut实操.md)
- [Content restructuring rules](artifact/references/内容层重组.md)
- [Generated footage guidance](artifact/references/生成素材.md)
- [Editing criteria](artifact/references/规则卡.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Video-editing project]

**Output Format:** [Markdown edit plan or editable ChatCut timeline; optional video export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Only deletes or reorders spoken words; exports and paid generation require explicit approval.]

## Skill Version(s):

0.4.5 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
