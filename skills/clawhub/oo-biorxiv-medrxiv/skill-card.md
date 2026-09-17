## Description:

Provides access to bioRxiv and medRxiv preprints, publication links, and submission or usage statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and agents use this skill to query bioRxiv and medRxiv preprint records, publication links, and usage or submission statistics through the OOMOL oo CLI connector.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes pipe-to-shell installer commands from the internet.

Mitigation: Review and verify the oo CLI installer before running it; prefer a package-managed or otherwise verified installation path.

Risk: Connector requests route through OOMOL with a persistent oo login.

Mitigation: Confirm this routing and account posture is acceptable before using the connector for bioRxiv or medRxiv requests.

## Reference(s):

- [bioRxiv and medRxiv homepage](https://www.biorxiv.org/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-biorxiv-medrxiv)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before execution and returns oo CLI JSON responses with execution metadata.]

## Skill Version(s):

1.0.2 (source: skill metadata and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
