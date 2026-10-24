## Description:

Helps Go developers use the unofficial go-zeroentropy client for ZeroEntropy retrieval, reranking, embeddings, and account operations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add the unofficial ZeroEntropy Go client to projects and write authenticated code for search, reranking, embeddings, and account management.

### Deployment Geography for Use:

Global; select the API region where the user's data resides.

## Known Risks and Mitigations:

Risk: An unofficial Go dependency and live API requests may access the wrong account or data region.

Mitigation: Confirm that the module and ZeroEntropy account are trusted, and choose the API host for the user's data region.

Risk: API keys and document download tokens could be exposed in code or logs.

Mitigation: Keep credentials out of source control and logs; load the API key from the environment.

Risk: Collection, document, organization, or API-key changes affect the account; queries and model calls may incur charges.

Mitigation: Make account changes only when explicitly requested, and review live requests before running them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-zeroentropy)
- [Go client package documentation](https://pkg.go.dev/github.com/psyb0t/go-zeroentropy)
- [Skill setup and API reference](artifact/references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the Go toolchain and a user-provided ZeroEntropy API key for live requests.]

## Skill Version(s):

0.1.1 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
