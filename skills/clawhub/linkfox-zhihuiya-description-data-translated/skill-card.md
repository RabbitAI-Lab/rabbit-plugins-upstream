## Description: <br>
Retrieves translated patent description/specification text from the Zhihuiya data service for a single patent in Chinese, English, or Japanese. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve translated patent specification text for a single known patent by patent ID or publication number, with optional family-member substitution when the original description is unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent queries and returned descriptions may contain confidential information sent to the LinkFox gateway. <br>
Mitigation: Use only an intended LinkFox API key and avoid submitting confidential patent data unless approved for that service. <br>
Risk: Full API responses are saved and cached locally, which can retain translated patent text beyond the immediate interaction. <br>
Mitigation: Review local LinkFox session data and cache files after use, and remove sensitive saved responses when retention is not needed. <br>
Risk: The artifact describes automatic feedback reporting and onboarding-skill installation paths. <br>
Mitigation: Require user approval before installing additional skills or sending feedback that may include user intent, interaction details, or patent content. <br>
Risk: Each API call can consume paid credits, and repeated patent requests can create unexpected cost. <br>
Mitigation: Process one patent per request, rely on the 24-hour cache for duplicate parameters, and obtain explicit consent before making multiple calls. <br>


## Reference(s): <br>
- [智慧芽-说明书翻译 API Reference](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-description-data-translated) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; API responses are JSON and may be summarized in stdout with full JSON saved to local files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Single patent per request; supports en, cn, and jp translations; uses a 24-hour cache and writes full responses under LinkFox session data.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
