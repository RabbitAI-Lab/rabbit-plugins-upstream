## Description:

Inventories office-agent skills, estimates their context cost, identifies possible duplicates, and offers conservative guidance on which skills to keep or review for closure.

This skill is ready for commercial/non-commercial use.

## Publisher:

[elisabeth15501](https://clawhub.ai/user/elisabeth15501)

### License/Terms of Use:

MIT-0

## Use Case:

Office-agent users and administrators can audit installed skills, estimate context-token use, identify possible duplicates, and review dependencies before deciding whether to disable a skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inventory reads local skill directories and related configuration, which may contain sensitive information.

Mitigation: Review the requested scan paths and share reports only with intended recipients.

Risk: Applying a close list can persistently disable WorkBuddy skills needed by other workflows.

Mitigation: Review candidates and dependencies first; use the host UI where possible, or explicitly confirm --overrides --apply --yes after reviewing the draft.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/elisabeth15501/skills/agent-skill-inventory)
- [Skill trigger taxonomy and telemetry limitations](artifact/references/usage-triggers.en.md)

## Skill Output:

**Output Type(s):** [Text, Guidance, JSON, Shell commands]

**Output Format:** [Plain-text inventory report or structured JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports support Chinese or English; JSON keys remain English.]

## Skill Version(s):

1.3.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
