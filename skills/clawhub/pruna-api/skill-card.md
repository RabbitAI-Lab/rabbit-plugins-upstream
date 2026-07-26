## Description: <br>
Use before any Pruna or Replicate HTTP call -- credentials, upload/poll/download, parallel batches, and agent safety. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare Pruna and Replicate API work, including credential checks, upload and polling flows, output downloads, parallel batch guidance, and safety review before paid calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the skill can send selected images, audio, portraits, scripts, or other media to Pruna or Replicate. <br>
Mitigation: Confirm user acknowledgement before uploads or paid predictions, and use only files the user intends to send to remote providers. <br>
Risk: API calls can incur paid usage. <br>
Mitigation: Check required environment variables and confirm intent before paid POST calls or generation runners. <br>
Risk: API keys could be exposed through prompts, logs, manifests, or subagent task text. <br>
Mitigation: Keep keys in host environment variables, never embed full keys in chat or files, and avoid distributing credentials to parallel subagents unless isolated secret injection is documented. <br>
Risk: Downloads or generated outputs can overwrite local files. <br>
Mitigation: Confirm output paths before writing or downloading files and avoid clobbering unrelated paths. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/pruna-api) <br>
- [API credentials](references/api-credentials.md) <br>
- [Agent safety](references/agent-safety.md) <br>
- [Pruna P-API shared reference](references/pruna-api.md) <br>
- [Pruna models index](references/pruna-models.md) <br>
- [Replicate API minimal reference](references/replicate-api.md) <br>
- [Pruna Developer Portal](https://docs.api.pruna.ai/) <br>
- [Pruna Quickstart](https://docs.api.pruna.ai/guides/quickstart) <br>
- [Pruna available models](https://docs.api.pruna.ai/guides/models) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration, code] <br>
**Output Format:** [Markdown guidance with inline shell commands and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include curl examples, environment variable names, polling guidance, and safety checks before paid API calls.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
