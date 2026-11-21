## Description:

Provides typed Go methods for calling the Fireworks AI Gateway and inference REST APIs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[psyb0t](https://clawhub.ai/user/psyb0t)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to add or maintain Go code that calls Fireworks AI inference endpoints and control-plane APIs, including guidance for authentication and typed responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, datasets, and model files sent in API requests reach Fireworks AI.

Mitigation: Review request contents and destination before sending; avoid transmitting sensitive material unless its use is approved.

Risk: The security evidence reports an unresolved local reference, leaving some assessment evidence incomplete.

Mitigation: Review the linked setup and package documentation before relying on the assessment or integrating the client.

## Reference(s):

- [Setup and reference](references/setup.md)
- [go-fireworks project repository](https://github.com/psyb0t/go-fireworks)
- [go-fireworks package documentation](https://pkg.go.dev/github.com/psyb0t/go-fireworks)

## Skill Output:

**Output Type(s):** [Go code, Shell commands, API usage guidance]

**Output Format:** [Markdown with Go and shell code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Setup and usage guidance for Fireworks AI control-plane and inference APIs.]

## Skill Version(s):

0.2.2 (source: evidence.json release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
