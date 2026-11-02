## Description:

Moonshot AI thinking model with text, image, and video understanding. Suited to complex analysis, coding, and writing that needs long reasoning chains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can send prompts to the Kimi K3 model for complex analysis, coding, and writing, with optional image and video inputs for understanding tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and parameters are sent to dLazy's hosted API, and selected local media files may be uploaded to its media storage.

Mitigation: Use the service only with content you are comfortable sending to dLazy; review the service terms before submitting sensitive prompts or media.

Risk: The CLI saves an API key in its local configuration, and requests can consume paid credits.

Mitigation: Protect the saved key, rotate or revoke it when needed, and use --dry-run to review the payload and cost estimate before making a request.

## Reference(s):

- [CLI project page (linked in skill metadata)](https://github.com/dlazy-ai/cli)
- [@dlazy/cli on npm](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, JSON, Guidance]

**Output Format:** [Text or structured JSON returned by the model]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Output depends on the prompt; image and video can be supplied as inputs for understanding.]

## Skill Version(s):

1.2.31 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
