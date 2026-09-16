## Description:

FullContact lets agents query FullContact through an OOMOL-connected account for company enrichment, person enrichment, and identity verification tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agents use this skill to run FullContact enrichment and identity verification actions through OOMOL-connected credentials without handling raw API tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup instructs users to execute remote installer scripts directly without verification.

Mitigation: Review the installer path before installation and prefer a verified, pinned, or signed distribution method for the oo CLI.

Risk: FullContact enrichment and verification can process personal identifiers.

Mitigation: Submit personal identifiers only with consent and a valid reason to process them through both OOMOL and FullContact.

Risk: Connector payloads may drift as FullContact action contracts change.

Mitigation: Inspect the live connector schema before each action and build payloads to match the returned contract.

## Reference(s):

- [FullContact homepage](https://www.fullcontact.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live connector schema inspection before each action; connector responses include data and meta.executionId.]

## Skill Version(s):

1.0.3 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
