## Description:

Use this skill to search and read Scopus abstracts, affiliations, authors, documents, and serial-source data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and developers use this skill to query Scopus for publications, authors, affiliations, abstracts, and sources without handling raw Scopus credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes an unverified internet installer executed directly in a shell.

Mitigation: Review setup before installing; prefer a pinned or signed oo CLI release, or verify the installer before running it.

Risk: The skill should normally stay within the listed read-only Scopus actions.

Mitigation: Require explicit user confirmation before any connector action that changes or deletes data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-scopus)
- [Scopus homepage](https://www.scopus.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with bash, PowerShell, text links, and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses include data and meta.executionId fields.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
