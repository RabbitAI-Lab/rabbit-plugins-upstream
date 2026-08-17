## Description:

This skill helps agents search and read public bioRxiv and medRxiv preprint data through the OOMOL bioRxiv/medRxiv connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and agents use this skill to retrieve public bioRxiv and medRxiv preprint records, publication links, and content or usage statistics. It is suited for literature discovery and metadata lookup workflows that need schema-checked connector calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connector payloads and lookups are routed through the OOMOL oo connector.

Mitigation: Use the skill for public preprint and metadata searches, and avoid including private or unrelated data in connector payloads.

Risk: The skill may require installing and signing in to the oo CLI before connector actions work.

Mitigation: Follow the first-time setup steps only after a command fails for a missing CLI or authentication reason.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-biorxiv-medrxiv)
- [bioRxiv and medRxiv homepage](https://www.biorxiv.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include connector response summaries and setup guidance when the oo CLI is missing or not signed in.]

## Skill Version(s):

1.0.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
