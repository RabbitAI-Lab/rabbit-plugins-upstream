## Description:

Beebole helps agents work with Beebole account data through an OOMOL-connected oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to inspect Beebole connector schemas and run Beebole GraphQL queries or mutations against an OOMOL-connected Beebole account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill advertises read-oriented use while allowing GraphQL mutations.

Mitigation: Review the exact GraphQL payload and expected effect before allowing mutations, and prefer read-only Beebole credentials when available.

Risk: Beebole requests and results are routed through OOMOL-connected infrastructure.

Mitigation: Use the skill only when this routing is acceptable for the account data involved.

Risk: The first-time setup section includes remote installer commands.

Mitigation: Independently verify installer source and integrity before running remote installation commands.

## Reference(s):

- [ClawHub Beebole skill page](https://clawhub.ai/oomol/skills/oo-beebole)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Beebole homepage](https://beebole.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Beebole connector responses as JSON when actions are run.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
