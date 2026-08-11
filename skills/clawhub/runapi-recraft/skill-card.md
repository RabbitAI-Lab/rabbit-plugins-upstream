## Description:

Generate and edit images with Recraft through RunAPI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[runapi-ai](https://clawhub.ai/user/runapi-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to generate, edit, upscale, or remove backgrounds from images with Recraft through RunAPI. It guides agents to use the RunAPI CLI for one-off work and SDKs for application or backend integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image prompts, source images, generated outputs, and account credentials may be handled by RunAPI/Recraft during use.

Mitigation: Use the skill only when the user accepts that provider handling; prefer RUNAPI_API_KEY or saved CLI configuration and avoid interactive browser login in headless agent runs.

Risk: Returned RunAPI file URLs are temporary and should not be treated as durable storage.

Mitigation: Download and store generated images or edited files in user-controlled durable storage within 7 days.

Risk: Using the CLI as a production runtime integration layer can create brittle application behavior.

Mitigation: Use the appropriate RunAPI SDK package for app, backend, worker, library, or webhook integrations.

## Reference(s):

- [RunAPI Recraft model page](https://runapi.ai/models/recraft)
- [Recraft model documentation](https://runapi.ai/models/recraft.md)
- [Recraft provider documentation](https://runapi.ai/providers/recraft.md)
- [RunAPI model catalog](https://runapi.ai/models.md)
- [RunAPI CLI skill](https://github.com/runapi-ai/cli-skill)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands and SDK package names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May direct agents to produce RunAPI request files, CLI commands, SDK integration code, and generated image assets returned by RunAPI/Recraft.]

## Skill Version(s):

0.2.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
