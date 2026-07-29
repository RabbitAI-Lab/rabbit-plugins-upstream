## Description: <br>
Use before any Pruna or Replicate HTTP call: credentials, upload/poll/download, parallel batches, and agent safety. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill before Pruna or Replicate generation work to handle API credentials, uploads, polling, downloads, parallel batch patterns, and safety checks for paid media calls. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local media, prompts, portraits, voices, and generated content may be sent to Pruna or Replicate services. <br>
Mitigation: Use the skill only when remote Pruna or Replicate generation is intended, and obtain explicit user acknowledgment before uploads or paid predictions. <br>
Risk: API credentials can be exposed if copied into chat, prompts, manifests, logs, or committed files. <br>
Mitigation: Keep PRUNA_API_KEY and REPLICATE_API_TOKEN in environment variables or a private .env file, and never include full keys in generated text or repository files. <br>
Risk: Paid calls and downloads can incur cost or overwrite local files. <br>
Mitigation: Confirm required credentials, upload content, paid-call intent, and output paths before making requests or writing downloaded files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/pruna-api) <br>
- [Pruna API reference](references/pruna-api.md) <br>
- [API credentials](references/api-credentials.md) <br>
- [Agent safety](references/agent-safety.md) <br>
- [Replicate API reference](references/replicate-api.md) <br>
- [Pruna models index](references/pruna-models.md) <br>
- [Pruna Developer Portal](https://docs.api.pruna.ai/) <br>
- [Pruna Quickstart](https://docs.api.pruna.ai/guides/quickstart) <br>
- [Pruna models](https://docs.api.pruna.ai/guides/models) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes credential checks, upload/poll/download patterns, and remote API safety prompts.] <br>

## Skill Version(s): <br>
1.0.8 (source: server evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
