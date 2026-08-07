## Description: <br>
Use before any Pruna or Replicate HTTP call: credentials, upload/poll/download, parallel batches, and agent safety. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to prepare authenticated Pruna P-API and Replicate calls, including credential checks, file uploads, async polling, downloads, and safety review before paid media generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can lead an agent to make paid Pruna or Replicate calls and upload local media to remote providers. <br>
Mitigation: Confirm required API keys, user authorization for submitted content, and explicit acknowledgment before the first upload or prediction. <br>
Risk: API keys could be exposed if copied into prompts, logs, manifests, or subagent task text. <br>
Mitigation: Read PRUNA_API_KEY and REPLICATE_API_TOKEN from the host environment only, avoid printing full keys, and do not embed secrets in generated files or messages. <br>
Risk: Downloaded outputs or runner files can overwrite local paths. <br>
Mitigation: Confirm output paths before writing downloads or generated files and avoid clobbering unrelated workspace content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pruna-ai/skills/pruna-api) <br>
- [API credentials](artifact/references/api-credentials.md) <br>
- [Agent safety](artifact/references/agent-safety.md) <br>
- [Pruna P-API shared reference](artifact/references/pruna-api.md) <br>
- [Replicate API minimal](artifact/references/replicate-api.md) <br>
- [Pruna models index](artifact/references/pruna-models.md) <br>
- [Pruna Developer Portal](https://docs.api.pruna.ai/) <br>
- [Pruna Quickstart](https://docs.api.pruna.ai/guides/quickstart) <br>
- [Pruna models](https://docs.api.pruna.ai/guides/models) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline shell commands and API request examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Guides paid remote API calls, media uploads, async polling, downloads, and credential handling.] <br>

## Skill Version(s): <br>
1.0.9 (source: evidence.release.version, SKILL.md metadata.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
