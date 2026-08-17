## Description:

DataCite (datacite.org). Use this skill for DataCite requests that search and read DOI metadata through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to retrieve a DOI metadata record or search, filter, sort, and page through DataCite DOI metadata via the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill relies on OOMOL and the oo CLI to access a user's DataCite-connected account.

Mitigation: Install and use it only when the user trusts OOMOL and has reviewed any first-time CLI installation or account connection step.

Risk: Authenticated lookups may expose non-public DOI metadata permitted by the connected API key.

Mitigation: Run only the intended read actions and review DOI identifiers, filters, and result scope before requesting authenticated metadata.

## Reference(s):

- [DataCite homepage](https://datacite.org/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-datacite)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the live connector schema before constructing action payloads.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
