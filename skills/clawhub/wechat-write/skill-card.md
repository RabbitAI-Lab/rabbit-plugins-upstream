## Description: <br>
公众号文案创作 helps agents search RedFox WeChat viral article data, analyze content patterns, and draft publish-ready WeChat Official Account articles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External content creators, content operators, MCN teams, and brand planners use this skill to research WeChat Official Account viral patterns and generate complete article drafts. It supports topic-based writing, product recommendation copy, trend analysis, and style adaptation from user-provided samples. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search keywords and timing filters are sent to redfox.hk. <br>
Mitigation: Use only non-sensitive topics and avoid confidential campaign plans, customer data, regulated information, or private writing samples. <br>
Risk: Security evidence reports an exposed real-looking API key. <br>
Mitigation: Review the release before installation and require the publisher to remove and rotate the exposed key before treating the package as clean. <br>
Risk: Security evidence flags a promotional contact line in generated output behavior. <br>
Mitigation: Review generated content before publication and remove any contact or promotional text that is not part of the intended article. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/wechat-write) <br>
- [公众号趋势数据格式说明](references/gzh_trend_data_format.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown article drafts with titles, body copy, tags, trend analysis, reference article summaries, and configuration guidance.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Drafts are grounded in RedFox WeChat trend data and may include references to searched article metrics; users can provide writing samples for style adaptation.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
