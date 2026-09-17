## Description:

Conductor helps agents query Conductor Monitoring data through an OOMOL-connected account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect live Conductor connector schemas and retrieve websites, pages, segments, issues, statistics, and affected-page data from a connected Conductor Monitoring account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup instructions include remote shell installer commands that execute downloaded scripts directly.

Mitigation: Prefer an official package manager, a pinned release, or a downloaded-and-verified installer before installing the oo CLI.

Risk: The skill depends on live connector schemas and an authenticated OOMOL connection, so requests may fail when authentication, scopes, connection state, or billing are unavailable.

Mitigation: Use the documented first-time setup and error-specific recovery steps only after an action fails for the matching reason.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-conductor)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Conductor Homepage](https://www.conductor.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-oriented connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are structured as JSON with data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
