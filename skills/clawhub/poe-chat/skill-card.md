## Description: <br>
Calls Poe models selected by @gemini, @gpt, @claude, and similar trigger words, chooses a concrete model_id, states the model used, and supports file uploads. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[longmans](https://clawhub.ai/user/longmans) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and external users use this skill to route prompts with model trigger words to Poe, list available Poe model IDs, and optionally attach local files for model analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts and files supplied with --file are sent to Poe and its model providers. <br>
Mitigation: Install only when that data sharing is intended, and avoid uploading secrets or regulated/private documents. <br>
Risk: Passing API keys directly on the command line can expose them through shell history or process listings. <br>
Mitigation: Prefer the POE_API_KEY environment variable for credential handling. <br>
Risk: Unpinned dependencies may change behavior before operational use. <br>
Mitigation: Pin reviewed dependency versions before using the skill operationally. <br>


## Reference(s): <br>
- [Poe Chat ClawHub skill page](https://clawhub.ai/longmans/skills/poe-chat) <br>
- [Poe models API](https://api.poe.com/v1/models) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown text with shell command examples and model response text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses begin by stating the selected Poe model; optional returned attachments are listed by name, content type, and URL.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
