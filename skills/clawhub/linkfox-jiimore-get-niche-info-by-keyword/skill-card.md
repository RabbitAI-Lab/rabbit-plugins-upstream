## Description: <br>
按关键词深度分析亚马逊细分市场，涵盖垄断程度、品牌集中度、新品成功率和市场机会评分。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Amazon sellers and ecommerce analysts use this skill to query Jiimore niche data by keyword and evaluate Amazon market segments for demand, competition, brand concentration, advertising cost, and new-product entry signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends Amazon keyword research, filters, API credentials, and session or app metadata to LinkFox services. <br>
Mitigation: Install and run it only in environments where sending those fields to LinkFox is acceptable, and use scoped API credentials. <br>
Risk: Full API responses may be saved locally, which can retain keyword research and returned market data beyond the immediate agent response. <br>
Mitigation: Review local workspace retention practices and remove saved response files when they are no longer needed. <br>
Risk: The Feedback API behavior can report user-derived context to a separate endpoint without an explicit prompt. <br>
Mitigation: Disable or avoid the feedback behavior where policy requires explicit approval before telemetry or user-context reporting. <br>


## Reference(s): <br>
- [Jiimore API reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-jiimore-get-niche-info-by-keyword) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API parameters, shell command examples, and tabular analysis of API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Full API responses are saved locally as JSON; large responses are summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.4 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
