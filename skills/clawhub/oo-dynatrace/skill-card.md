## Description:

Dynatrace helps agents search and read Dynatrace data through OOMOL's oo CLI connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and support engineers use this skill to inspect Dynatrace monitored entities and list problem data from an OOMOL-connected Dynatrace account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup includes unverified remote installer commands for the oo CLI.

Mitigation: Install the oo CLI through a verified, pinned, or platform-managed method before using the skill.

Risk: Dynatrace requests and responses are routed through OOMOL rather than direct API access.

Mitigation: Use the skill only when OOMOL mediation is acceptable for the sensitivity of the connected Dynatrace data.

## Reference(s):

- [Dynatrace ClawHub skill](https://clawhub.ai/oomol/skills/oo-dynatrace)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Dynatrace homepage](https://www.dynatrace.com)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with oo CLI shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live connector action schemas should be inspected before constructing payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
