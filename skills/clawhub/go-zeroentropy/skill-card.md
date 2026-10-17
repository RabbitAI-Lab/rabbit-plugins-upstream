## Description:

Guides developers using the unofficial ZeroEntropy Go client to write code for collections, documents, retrieval, reranking, embeddings, usage, and administration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate the unofficial ZeroEntropy Go client into Go projects for search, document management, model calls, usage reporting, and account administration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated code may change or delete account resources or API keys.

Mitigation: Review generated code before running it and approve account-changing calls only when requested.

Risk: Model queries may incur usage charges.

Mitigation: Confirm intended queries and likely cost before running generated code against the service.

Risk: API keys and document download tokens could be exposed in code or logs.

Mitigation: Use environment-provided credentials and avoid committing or logging keys, authorization headers, and token-bearing URLs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/psyb0t/skills/go-zeroentropy)
- [Setup and API guidance](references/setup.md)
- [Unofficial Go client repository](https://github.com/psyb0t/go-zeroentropy)
- [ZeroEntropy dashboard](https://dashboard.zeroentropy.dev/)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance for consuming an unofficial Go client; does not itself execute API requests.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
