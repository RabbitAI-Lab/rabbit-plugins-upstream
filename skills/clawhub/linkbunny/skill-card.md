## Description:

Helps site owners manage LinkBunny backlink assignments and propose relevant, owner-approved link placements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkbunny](https://clawhub.ai/user/linkbunny)

### License/Terms of Use:

MIT-0

## Use Case:

Site owners and their authorized agents use LinkBunny to register owned sites, review backlink assignments, and propose contextual nofollow links. Publication and assignment reporting require separate owner approval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed LinkBunny API token could allow unauthorized account-linked backlink actions.

Mitigation: Keep the token in an owner-approved private secret store; never print, share, or commit it.

Risk: Autonomous check-ins, billing changes, or site edits could act beyond the owner's intent.

Mitigation: Require specific owner authorization for each action; do not poll or make broad autonomous changes.

Risk: Irrelevant or unapproved backlink placements could compromise site content.

Mitigation: Review each placement before publication, keep it within the authorized site area, and use a contextual nofollow link.

## Reference(s):

- [LinkBunny agent documentation](https://getlinkbunny.com/docs/agents?ref=clawhub)
- [LinkBunny skill release](https://clawhub.ai/linkbunny/skills/linkbunny)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown with proposed placements and optional commands or site edits]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Link placements require owner approval; completion reports are self-reported.]

## Skill Version(s):

1.1.0 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
