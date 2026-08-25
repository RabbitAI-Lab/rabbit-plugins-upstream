## Description:

This skill helps apparel and e-commerce teams produce diverse AI model catalog image sets from authorized product images, audience conditions, scene constraints, platform requirements, and AI-HIVE generation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External apparel brands, cross-border sellers, and marketing teams use this skill to plan and generate multi-skin-tone, multi-body-type model image sets for e-commerce, advertising, social commerce, and marketing campaigns. Developers and operators can use the bundled scripts to create production briefs, initialize AI-HIVE API access, upload authorized references, submit image generation tasks, poll status, and download generated outputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Selected images and prompts can be uploaded to AI-HIVE.

Mitigation: Use only media and prompt content the user is authorized to upload, and avoid including private or sensitive material unless the user has approved that transfer.

Risk: Image generation can submit paid AI-HIVE tasks.

Mitigation: Show the final prompt, model, routing mode, batch size, parameters, and price snapshot before running generation, and start with a small sample batch.

Risk: API keys can be exposed through project files, logs, screenshots, or shared command history.

Mitigation: Use environment variables or the local AI-HIVE config file, keep config permissions restricted, and never commit or echo real keys.

Risk: Generated synthetic model images can create misleading authenticity, body-effect, endorsement, or platform-compliance claims.

Mitigation: Require human review for product accuracy, synthetic-person disclosure, authorization, platform rules, and any factual claims before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wubin1836/skills/diverse-model-catalog-images-ai-hive)
- [AI-HIVE chat and API access](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base endpoint](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance, files]

**Output Format:** [Markdown guidance with shell command examples, JSON production briefs, API task records, and downloaded image files when generation is executed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create a local API-key configuration file, upload selected references to AI-HIVE, poll asynchronous tasks, and download generated media to a local output directory.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
