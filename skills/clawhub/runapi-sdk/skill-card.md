## Description:

Choose RunAPI SDK packages for application developers building web apps, backends, workers, or libraries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to choose and wire up RunAPI SDK packages for JavaScript, Python, Ruby, Go, Java, or PHP application integrations. It helps agents distinguish production SDK integration from one-off CLI-driven media generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated integration guidance may reference SDK documentation and package READMEs that change over time.

Mitigation: Review the current RunAPI SDK documentation and package README for the selected language and provider before shipping an integration.

Risk: RunAPI API keys could be exposed if copied into source code or logs.

Mitigation: Keep RUNAPI_API_KEY in environment variables or secret storage and avoid committing or logging secrets.

Risk: Returned generated-file URLs are temporary and may expire before an application stores them.

Mitigation: Download generated images, videos, audio, or other files into durable application storage within the documented retention window.

## Reference(s):

- [RunAPI model and SDK catalog](https://runapi.ai/models.md)
- [RunAPI models homepage](https://runapi.ai/models)
- [ClawHub skill page](https://clawhub.ai/runapi-ai/skills/runapi-sdk)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with package names, install commands, code snippets, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May refer to RunAPI SDK package READMEs and documentation for language-specific client methods, response shapes, and errors.]

## Skill Version(s):

0.2.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
