## Description:

Harmonic.ai lets an agent use an OOMOL-connected Harmonic.ai account to search, enrich, and retrieve company and person data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, business operations teams, and external agents use this skill to retrieve Harmonic.ai company or person profiles, list company employee URNs, check enrichment status, and request enrichment through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that may be unsafe if run automatically.

Mitigation: Install the oo CLI through a verified or manual process, and run setup only after a matching missing-command, authentication, or connection error.

Risk: Enrichment actions may use Harmonic.ai account resources or create remote enrichment jobs.

Mitigation: Confirm the exact enrichment payload and expected account effect with the user before running enrichment actions.

Risk: Connector authentication, connection scope, or billing state can block action execution.

Mitigation: Use the OOMOL account connection and billing pages only when the corresponding error is returned, then retry after the user resolves the account state.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-harmonic-ai)
- [Harmonic.ai homepage](https://harmonic.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Action responses are returned as JSON; payloads are based on the connector schema inspected at runtime.]

## Skill Version(s):

1.0.2 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
