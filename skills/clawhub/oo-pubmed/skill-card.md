## Description:

PubMed enables agents to search PubMed and retrieve normalized biomedical article data through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search PubMed, retrieve article records by PMID, convert biomedical article identifiers, find related or citing articles, inspect references, and match raw biomedical citations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer commands for the oo CLI.

Mitigation: Prefer official installation documentation, inspect downloaded scripts or signed packages where available, and avoid running installer commands from an elevated shell unless intentionally trusted.

Risk: The skill depends on OOMOL's oo CLI and PubMed connector.

Mitigation: Install only when use of the OOMOL CLI and connector is acceptable for the target environment.

## Reference(s):

- [ClawHub PubMed Skill](https://clawhub.ai/oomol/skills/oo-pubmed)
- [PubMed Homepage](https://pubmed.ncbi.nlm.nih.gov/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads or results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an installed, signed-in oo CLI and a connected PubMed account.]

## Skill Version(s):

1.0.2 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
