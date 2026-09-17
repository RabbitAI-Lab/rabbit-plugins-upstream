## Description:

Dandelion API (dandelion.eu). Use this skill for ANY Dandelion API request - searching and reading data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to operate Dandelion API through an OOMOL-connected account for sentiment analysis, semantic text similarity, language detection, and linked entity extraction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could execute mutable code on the user's machine.

Mitigation: Review the oo CLI installation path and prefer an official package manager or installer with checksum or signature verification before installation.

Risk: Text sent for analysis may be processed by OOMOL and Dandelion services.

Mitigation: Only connect the OOMOL and Dandelion accounts intentionally, and avoid sending sensitive text unless that processing is acceptable.

Risk: Connector requests can fail when authentication, app connection, scopes, credentials, or billing are unavailable.

Mitigation: Use the skill's documented recovery flow for auth, connection, scope, credential, app readiness, and billing errors before retrying.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-dandelion)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Dandelion API homepage](https://dandelion.eu/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses when actions are run with --json.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
