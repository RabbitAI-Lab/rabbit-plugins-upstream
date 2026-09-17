## Description:

PubMed enables agents to search PubMed and retrieve normalized biomedical article data through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research workflows use this skill to search PubMed, look up PubMed articles by PMID, resolve article identifiers, and retrieve related, referenced, or citing biomedical literature records.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup recommends running remote installer scripts directly in a shell.

Mitigation: Review setup steps before installation and prefer a verified, signed, or package-manager-based oo CLI install path.

Risk: PubMed searches, PMIDs, raw citations, and returned article metadata may be processed by OOMOL.

Mitigation: Avoid sensitive health, personal, or confidential research queries unless OOMOL processing is approved for the use case.

Risk: Live PubMed citation, reference, and related-article coverage can be incomplete.

Mitigation: Treat returned literature relationships as retrieval results and verify important biomedical conclusions against primary sources.

## Reference(s):

- [PubMed homepage](https://pubmed.ncbi.nlm.nih.gov/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI install guide](https://cli.oomol.com/install-guide.md)
- [PubMed connection settings](https://console.oomol.com/app-connections?provider=pubmed)
- [ClawHub PubMed skill listing](https://clawhub.ai/oomol/skills/oo-pubmed)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill fetches live action schemas before constructing connector payloads.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
