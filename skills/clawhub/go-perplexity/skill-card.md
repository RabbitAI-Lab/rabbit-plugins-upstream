## Description:

Helps Go developers use the typed go-perplexity client to call Perplexity API endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to install the go-perplexity package and write typed calls for Perplexity chat, search, embeddings, agents, skills, decisions, models, and usage endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API calls can incur costs and some operations can change account state.

Mitigation: Make billed or state-changing calls only when the user asks, and limit changes to resources the user named or the task created.

Risk: The security review reports an unresolved local reference and a disputed tool-use alert, so some evidence is incomplete.

Mitigation: Review the unresolved reference and disputed alert before installation; treat the benign verdict as a scanner result, not a safety guarantee.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [go-perplexity project](https://github.com/psyb0t/go-perplexity)
- [go-perplexity package documentation](https://pkg.go.dev/github.com/psyb0t/go-perplexity)
- [ClawHub release page](https://clawhub.ai/psyb0t/skills/go-perplexity)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Installation steps, endpoint and type reference, and usage examples.]

## Skill Version(s):

0.4.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
