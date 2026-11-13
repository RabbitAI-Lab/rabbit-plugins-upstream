## Description:

An unofficial Go client for the Perplexity REST API that provides typed methods for chat, search, embeddings, agents, skills, decisions, models, and usage analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this client to integrate Perplexity API endpoints into applications, with typed requests and responses and bearer-key authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security scan found no confirmed harmful behavior, but confidence is medium and coverage is partial because a local reference could not be resolved.

Mitigation: Resolve and review the missing reference, then review the full release before relying on the scan result.

Risk: Perplexity requests use an API key; calls can incur charges or change account state.

Mitigation: Read the key from an environment variable, never commit, log, or print it, and review state-changing or billable calls before making them.

## Reference(s):

- [Setup and reference](artifact/references/setup.md)
- [Source repository](https://github.com/psyb0t/go-perplexity)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-perplexity)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with Go code and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.3.6 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
