## Description:

Guides developers using a typed Go client to call the Contextual AI API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate the Contextual AI API for agent queries, datastores, documents, generation, parsing, and reranking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Delete, reset, user removal, ingestion, and parse-upload calls can change account data.

Mitigation: Run these operations only at the user's direction and confirm the affected resources.

Risk: API credentials or request data could be exposed through unsafe code or an untrusted API endpoint.

Mitigation: Keep the bearer key in an environment variable, avoid logging it, and use a trusted HTTPS base URL.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/psyb0t/skills/go-contextual-ai)
- [Setup and API reference](references/setup.md)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go code and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Provides typed client usage and guidance for handling API responses.]

## Skill Version(s):

0.1.1 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
