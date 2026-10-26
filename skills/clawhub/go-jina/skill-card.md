## Description:

Provides typed Go clients for Jina AI's embeddings, reranking, chat completion, batch embedding, and Reader APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Go developers use this skill to integrate Jina AI's hosted embedding, reranking, chat-completion, batch, and Reader APIs into Go projects, including configuring bearer-key authentication.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Text, images, documents, and URLs sent through the client are shared with Jina AI's hosted services.

Mitigation: Send only data the user approves sharing with Jina AI.

Risk: The JINA_API_KEY is a bearer credential.

Mitigation: Read it from the environment; never hardcode, commit, or log it, including in Authorization headers.

Risk: Batch embedding jobs can incur charges, and cancellation changes job state.

Mitigation: Create or cancel only jobs the user explicitly authorized and the task owns.

## Reference(s):

- [Setup and API reference](references/setup.md)
- [Project homepage](https://github.com/psyb0t/go-jina)
- [Go package documentation](https://pkg.go.dev/github.com/psyb0t/go-jina)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Guidance]

**Output Format:** [Go code and Markdown guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Examples configure API-key authentication and show typed requests and response handling.]

## Skill Version(s):

0.3.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
