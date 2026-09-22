## Description:

Score startup idea through S.E.E.D. niche check + STREAM 6-layer analysis + Devil's Advocate inversion, auto-pick stack, and generate PRD with acceptance criteria.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fortunto2](https://clawhub.ai/user/fortunto2)

### License/Terms of Use:

MIT

## Use Case:

External founders, product builders, and developers use this skill to evaluate startup ideas, identify kill flags, select an implementation stack, and generate a PRD with acceptance criteria.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests local search and shell access that may expose private Markdown notes or workspace data.

Mitigation: Use it only in a workspace where local note search is acceptable, or run it in a scoped workspace with limited files.

Risk: The skill can write a PRD file without explicit save confirmation.

Mitigation: Confirm the intended PRD path before use and review generated files before committing or sharing them.

Risk: The security verdict is suspicious due to broad tool access relative to the workflow.

Mitigation: Review the skill before installation and consider removing Bash or other broad tools when they are not needed.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/fortunto2/skills/solo-validate)
- [Manifest Alignment Checklist](artifact/references/manifest-checklist.md)
- [STREAM 6-Layer Framework](artifact/references/stream-layers.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with optional generated PRD file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write docs/prd.md after idea validation and stack selection.]

## Skill Version(s):

2.1.1 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
