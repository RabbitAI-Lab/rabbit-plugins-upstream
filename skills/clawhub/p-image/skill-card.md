## Description: <br>
Use when someone explicitly wants the fastest, cheapest photo generation - mood boards, bulk panels, or quick iterations - not when controlled photoreal or in-image text is needed. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pruna-ai](https://clawhub.ai/user/pruna-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and agent operators use this skill to route simple, quick photo-generation requests to Pruna's p-image API, draft faithful prompts, choose an aspect ratio, and produce the curl command pattern for asynchronous generation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated prompts and related image data may be sent to Pruna's external API, and API usage may incur cost. <br>
Mitigation: Confirm PRUNA_API_KEY setup, review prompts before submission, and use the asynchronous generation flow intentionally before making paid API calls. <br>
Risk: Companion Pruna skills can affect credential handling and upload, polling, or download behavior. <br>
Mitigation: Review companion skills separately before installation or use, especially the API helper skill. <br>


## Reference(s): <br>
- [ClawHub p-image skill page](https://clawhub.ai/pruna-ai/skills/p-image) <br>
- [Pruna predictions API endpoint](https://api.pruna.ai/v1/predictions) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash curl commands and API request parameters] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires PRUNA_API_KEY and may use optional image-generation parameters such as aspect_ratio and seed.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
