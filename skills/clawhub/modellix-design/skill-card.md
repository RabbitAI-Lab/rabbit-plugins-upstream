## Description:

Integrate Modellix's unified API for AI image, video, and audio workflows. Use this skill whenever the user wants to generate or edit images, create or transform videos, synthesize speech, transcribe audio, clone a voice, do virtual try-on, or call any Modellix model API. Also trigger when the user mentions Modellix, model-as-a-service for media generation, or providers such as Qwen, Wan, Seedream, Seedance, Kling, Hailuo, MiniMax, Whisper, or CosyVoice through a unified API, or when they ask for a Modellix model's request schema, OpenAPI contract, or required input fields. When the Modellix Media Generation MCP tools are available and the input is not a local file, submit through that MCP. Otherwise prefer modellix-cli (model get-schema, model run --wait, task download, doctor, model list). Use REST only when both the Media Generation MCP and the CLI are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modellix](https://clawhub.ai/user/modellix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use this skill to discover Modellix model schemas and run image, video, and audio generation or processing workflows through the Media Generation MCP, the CLI, or REST when the preferred interfaces are unavailable. It also provides setup and credential guidance for those workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI workflow can automatically replace shared software before execution.

Mitigation: Set MODELLIX_CLI_AUTO_UPDATE=0 and use a reviewed CLI version, preferably in an isolated environment.

Risk: A documented profile-clearing command removes a saved profile without confirmation.

Mitigation: Do not run the profile-clearing example unless you intend to remove that profile.

Risk: Prompts and selected media leave the local environment, and generation is billed.

Mitigation: Send only content approved for the remote service and confirm expected costs before submitting generation tasks.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/modellix/skills/modellix-design)
- [Modellix AI onboarding](https://docs.modellix.ai/get-started.md)
- [Modellix REST API](https://docs.modellix.ai/ways-to-use/api.md)
- [Modellix model index](https://docs.modellix.ai/llms.txt)
- [Modellix Docs Search MCP](https://docs.modellix.ai/mcp)
- [Modellix Media Generation MCP](https://tool.modellix.ai/mcp/media)
- [modellix-cli package](https://www.npmjs.com/package/modellix-cli)
- [CLI playbook](references/cli-playbook.md)
- [Media MCP playbook](references/media-mcp-playbook.md)
- [REST playbook](references/rest-playbook.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance, API calls, Files]

**Output Format:** [Markdown guidance with shell commands, configuration and JSON request examples; workflow results may include downloadable image, video, or audio files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media tasks are asynchronous; output files and formats depend on the selected model.]

## Skill Version(s):

1.0.6 (source: server-resolved ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
