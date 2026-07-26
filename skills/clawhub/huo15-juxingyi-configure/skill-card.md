## Description: <br>
Configures Juxingyi as an OpenClaw model provider by calling the Juxingyi /v1/models endpoint with an fsk- API key and writing the returned text model list into openclaw.json. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zhaobod1](https://clawhub.ai/user/zhaobod1) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
OpenClaw users and developers use this skill to add or refresh the Juxingyi fireworks-hub provider, list available models, and switch the primary model without manually editing the provider configuration. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill contacts Juxingyi with the user's fsk- API key to retrieve available models. <br>
Mitigation: Install and run it only when you intend to configure the Juxingyi provider, and use a key with appropriate permissions. <br>
Risk: The default configuration path can store the API key directly in openclaw.json. <br>
Mitigation: Use the --env option to store a FIREWORKS_API_KEY environment variable reference instead of writing the key value into the configuration file. <br>
Risk: The script updates the local OpenClaw model configuration. <br>
Mitigation: Review the generated backup path and keep the backup until the updated provider configuration has been verified. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zhaobod1/skills/huo15-juxingyi-configure) <br>
- [Juxingyi integration documentation](https://fireworks-simulator.huo15.com/docs.html) <br>
- [Juxingyi console](https://fireworks-simulator.huo15.com/app/) <br>
- [User guide](docs/user-guide.md) <br>
- [Developer guide](docs/dev-guide.md) <br>
- [Product requirements](docs/prd.md) <br>
- [Changelog](docs/changelog.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and OpenClaw JSON configuration changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local OpenClaw provider updates and backup paths; model data is fetched live from Juxingyi rather than bundled in the skill.] <br>

## Skill Version(s): <br>
1.3.0 (source: SKILL.md frontmatter, _meta.json, evidence release, changelog released 2026-07-19) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
