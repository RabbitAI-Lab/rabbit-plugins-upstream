## Description:

Helps developers write Go code using an unofficial typed client for the Contextual AI API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to integrate Contextual AI services into Go applications, including agent queries, document ingestion, and datastore management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Exposing a Contextual AI bearer key in generated code or logs.

Mitigation: Load the key from an environment variable or secret manager; never commit or log it.

Risk: Generated calls may delete, reset, remove, invite, or ingest account resources.

Mitigation: Review these operations and their targets before running them; perform only changes the user requested.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-contextual-ai)
- [Go client homepage](https://github.com/psyb0t/go-contextual-ai)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples use typed API responses and bearer-key authentication.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
