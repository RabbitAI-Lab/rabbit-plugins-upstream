## Description:

Harmonic.ai helps agents enrich and retrieve company and person data through OOMOL-backed Harmonic.ai actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to enrich company or person records, retrieve Harmonic.ai profiles, list company employee person URNs, and check enrichment status through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Use official, versioned installation instructions with checksum or signature verification, and get explicit approval before installing the oo CLI.

Risk: Enrichment requests can involve personal or business identifiers such as email addresses, LinkedIn URLs, websites, or company IDs.

Mitigation: Confirm the user is authorized to submit the requested identifiers to Harmonic.ai before running enrichment or lookup actions.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/oomol/skills/oo-harmonic-ai)
- [Harmonic.ai homepage](https://harmonic.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash, PowerShell, and JSON snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector action responses include a data object and meta.executionId when actions run.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
