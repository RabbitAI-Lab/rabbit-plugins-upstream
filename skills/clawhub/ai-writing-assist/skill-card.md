## Description:

Uses the Flyelep AI writing API to generate creative copy, optimize prompts, and provide writing inspiration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[flyelepai](https://clawhub.ai/user/flyelepai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to collect a writing prompt and optional reference file URLs, call Flyelep's writing-assistance API, and present multiple creative copy options for prompt optimization, ecommerce copy, poster copy, or short-video scripts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and optional file URLs are sent to Flyelep for writing assistance.

Mitigation: Use the skill only for content appropriate to share with Flyelep, and avoid secrets, regulated data, private business material, or sensitive file URLs.

Risk: The Flyelep API key is required in the request header at call time.

Mitigation: Provide the API key only at runtime and do not store it in skill files, repositories, examples, or persistent configuration.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/flyelepai/skills/ai-writing-assist)
- [Flyelep assisted generation API](https://www.flyelep.cn/prod-api/poster-design/api/v1/aiTool/assistedGeneration)
- [Flyelep controlboard](https://www.flyelep.cn/controlboard)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns multiple generated copy options; query input is limited to 1000 characters and optional reference file URLs are limited to six files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
