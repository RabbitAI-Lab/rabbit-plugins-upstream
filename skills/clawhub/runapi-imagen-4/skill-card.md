## Description:

Generate and edit images with Imagen 4 through RunAPI. Use when the user asks an agent to create, edit, or transform images with Imagen 4. Default to the RunAPI CLI for one-off generation; use SDKs only when the user is integrating RunAPI into an app or backend.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate, edit, and transform images with Imagen 4 through RunAPI. It guides one-off CLI use and SDK-based application integration while separating manual tasks from production runtime integration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or invoking the RunAPI CLI or SDK packages requires trust in a third-party publisher and may use an API key.

Mitigation: Confirm the user trusts RunAPI before installing dependencies or configuring RUNAPI_API_KEY, and prefer environment or saved CLI authentication for headless runs.

Risk: RunAPI-generated file URLs are temporary and should not be treated as long-term assets.

Mitigation: Download generated files to user-controlled durable storage within 7 days.

Risk: Using the CLI as a production integration layer can create brittle runtime behavior.

Mitigation: Use the SDK integration path for apps, backends, workers, libraries, services, and production workflows.

## Reference(s):

- [RunAPI Imagen 4 homepage](https://runapi.ai/models/imagen-4)
- [RunAPI Imagen 4 model overview, pricing, and rate limits](https://runapi.ai/models/imagen-4.md)
- [RunAPI Google provider page](https://runapi.ai/providers/google.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill guidance](https://github.com/runapi-ai/cli-skill)
- [Imagen 4 variant](https://runapi.ai/models/imagen-4/imagen-4.md)
- [Imagen 4 Fast variant](https://runapi.ai/models/imagen-4/fast.md)
- [Imagen 4 Ultra variant](https://runapi.ai/models/imagen-4/ultra.md)
- [Imagen 4 Pro remix image variant](https://runapi.ai/models/imagen-4/pro-remix-image.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples, SDK package names, and configuration notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agents to create image generation request files and to download temporary generated file URLs to durable storage within 7 days.]

## Skill Version(s):

0.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
