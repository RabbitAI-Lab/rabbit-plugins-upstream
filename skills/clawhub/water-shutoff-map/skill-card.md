## Description:

Use before a plumbing emergency, when moving into a new home, before DIY repairs, when a pipe bursts or a toilet overflows, or when creating a household emergency reference sheet; walks users through locating every water shutoff in a home, records findings into a durable JSON registry with photos, generates a printable emergency card, and gives a 3-step first response for floods, burst pipes, and overflowing fixtures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[voronindenis5](https://clawhub.ai/user/voronindenis5)

### License/Terms of Use:

MIT

## Use Case:

External users, homeowners, renters, landlords, and household maintainers use this skill to find, document, validate, and rehearse water shutoff procedures before or during home plumbing emergencies.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat plumbing preparation guidance as permission to force corroded or stuck valves, or operate shared building or municipal valves without authorization.

Mitigation: Do not force corroded or stuck valves; do not operate shared building or municipal valves unless authorized; contact a plumber, landlord, building staff, or utility when in doubt.

Risk: The skill maintains a local household shutoff registry that can include home utility locations, tool locations, photos, and emergency contact details.

Mitigation: Install and use only if comfortable maintaining that local registry; keep registry files and backups private and review generated cards before posting or sharing them.

## Reference(s):

- [Locating Water Shutoffs - The Hunting Guide](references/locating-shutoffs.md)
- [ClawHub skill page](https://clawhub.ai/voronindenis5/skills/water-shutoff-map)
- [Server-resolved source repository](https://github.com/voronindenis5/water-shutoff-map)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, plain text emergency cards, and JSON registry data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Writes a local household shutoff registry at ~/.shutoff-registry.json by default, with --file support for alternate registry paths.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
