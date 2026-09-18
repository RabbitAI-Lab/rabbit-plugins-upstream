## Description:

Provides Addressfinder address search, metadata lookup, and verification through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to search Australian and New Zealand addresses, retrieve selected address metadata, and verify or enrich address data through Addressfinder.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup directs users to execute mutable remote install scripts in shell interpreters.

Mitigation: Install the oo CLI through a verified, pinned, or signed distribution method before using the skill.

Risk: Address search, verification, and metadata payloads can contain personal address data.

Mitigation: Send only the fields required by the requested Addressfinder action and inspect the live action schema before submitting payloads.

Risk: Authentication or connection recovery can open account setup and billing flows.

Mitigation: Run login, connection, or billing steps only after a command fails for the matching reason and keep the user in control of those flows.

## Reference(s):

- [ClawHub Addressfinder Skill](https://clawhub.ai/oomol/skills/oo-addressfinder)
- [Addressfinder Homepage](https://addressfinder.com/au)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before submitting action payloads; Addressfinder action responses are JSON.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
