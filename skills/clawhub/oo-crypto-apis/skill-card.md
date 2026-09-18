## Description:

Crypto APIs lets agents search and read Crypto APIs market data through an OOMOL-connected account instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve Crypto APIs asset details, exchange rates, and supported asset lists through OOMOL-managed connector actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The first-time setup flow includes remote installer commands that execute downloaded code on the user's computer.

Mitigation: Review the oo CLI installation source before installing, and prefer an official signed package, pinned release, or manually downloaded installer with checksum or signature verification.

Risk: Connector actions depend on a signed-in OOMOL account and a connected Crypto APIs provider, so failed authentication, expired credentials, missing scopes, or billing stops can interrupt use.

Mitigation: Run setup steps only after a matching command failure, then resolve authentication, connection scope, credential, or billing errors in the OOMOL console before retrying.

## Reference(s):

- [Crypto APIs homepage](https://cryptoapis.io)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-crypto-apis)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects with data and execution metadata.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
