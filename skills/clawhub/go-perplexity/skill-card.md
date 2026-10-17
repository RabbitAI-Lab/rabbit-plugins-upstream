## Description:

Guides Go developers in using an unofficial typed client for Perplexity's chat, search, embeddings, and account APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers working on Go applications use this skill to integrate the Perplexity API, including chat completions, web search, embeddings, and other supported endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing the Perplexity API key in source code, logs, or request headers.

Mitigation: Keep PERPLEXITY_API_KEY in the environment or a secret manager; do not commit or log it.

Risk: API calls may incur charges or modify account resources, including skills and agent runs.

Mitigation: Require explicit user confirmation before cost-incurring, create, update, delete, cancel, or file-download operations.

Risk: Adding an unreviewed upstream Go dependency to a project.

Mitigation: Review the client and its dependencies before installation.

## Reference(s):

- [go-perplexity skill release](https://clawhub.ai/psyb0t/skills/go-perplexity)
- [Setup and API reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Covers API-key setup, typed requests, and response handling.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
