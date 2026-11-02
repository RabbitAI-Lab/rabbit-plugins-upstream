## Description:

Integrate Modellix's unified API for AI image, video, and audio workflows. Use this skill whenever the user wants to generate or edit images, create or transform videos, synthesize speech, transcribe audio, clone a voice, do virtual try-on, or call any Modellix model API. Also trigger when the user mentions Modellix, model-as-a-service for media generation, or providers such as Qwen, Wan, Seedream, Seedance, Kling, Hailuo, MiniMax, Whisper, or CosyVoice through a unified API, or when they ask for a Modellix model's request schema, OpenAPI contract, or required input fields. When the Modellix Media Generation MCP tools are available and the input is not a local file, submit through that MCP. Otherwise prefer modellix-cli (model get-schema, model run --wait, task download, doctor, model list). Use REST only when both the Media Generation MCP and the CLI are unavailable.

This skill is ready for commercial/non-commercial use.

## Publisher:

[modellix](https://clawhub.ai/user/modellix)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and creators use the skill to select a named Modellix model, check its request schema, and run or manage image, video, and audio tasks through the Media Generation MCP, CLI, or REST fallback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The CLI helper may replace a shared CLI, and a failed global update has no implemented rollback.

Mitigation: Review the automatic updater before use; set MODELLIX_CLI_AUTO_UPDATE=0 before running the helpers when you want to manage CLI versions yourself.

Risk: Prompts and media inputs are sent to Modellix, and generation can incur charges.

Mitigation: Submit only inputs intended for Modellix and confirm the selected model and request before starting a paid task.

## Reference(s):

- [ClawHub release](https://clawhub.ai/modellix/skills/modellix-design)
- [Modellix AI Onboarding](https://docs.modellix.ai/get-started.md)
- [Modellix REST API](https://docs.modellix.ai/ways-to-use/api.md)
- [Modellix CLI package](https://www.npmjs.com/package/modellix-cli)
- [Capability Matrix](references/capability-matrix.md)
- [CLI Playbook](references/cli-playbook.md)
- [Media Generation MCP](references/media-mcp-playbook.md)
- [REST Playbook](references/rest-playbook.md)

## Skill Output:

**Output Type(s):** [API calls, Shell commands, JSON, Generated media files, Guidance]

**Output Format:** [JSON task results and generated media files, with Markdown guidance and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Request fields depend on the user-selected model; media generation may incur charges.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata; skill frontmatter: 4.13.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
