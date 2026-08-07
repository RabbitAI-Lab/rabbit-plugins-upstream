## Description: <br>
Retrieves patent specification and full description data from the Zhihuiya patent database by patent ID or publication number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and patent-research users use this skill to retrieve full patent descriptions for one or more known patent IDs or publication numbers, including optional family-member substitution when the target description is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill performs LinkFox/Zhihuiya API calls that may consume credits. <br>
Mitigation: Confirm the lookup scope with the user before additional or repeated queries, especially for batch requests. <br>
Risk: The skill uses API keys from environment variables and writes full response data and cache files locally. <br>
Mitigation: Use only trusted execution environments, protect local output directories, and avoid sending sensitive patent data unless the user accepts the data-handling behavior. <br>
Risk: The security review flags automatic feedback reporting and onboarding ZIP installation behavior for review before installation. <br>
Mitigation: Allow feedback submission or onboarding installation only after explicitly trusting the LinkFox source and understanding what data may be sent or installed. <br>


## Reference(s): <br>
- [Zhihuiya Patent Description API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-description-data) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files, API Calls] <br>
**Output Format:** [Markdown guidance with JSON API parameters, shell command examples, and saved JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes full API responses and 24-hour cache files locally; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
