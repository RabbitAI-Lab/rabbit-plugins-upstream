## Description: <br>
Retrieves translated patent claim text from the Zhihuiya (PatSnap) patent database in Chinese, English, or Japanese by patent ID or publication number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patent professionals, researchers, and agents use this skill to retrieve translated claim text for one or more known patents by patent ID or publication number. It can optionally use related-family patent substitution when original claims are unavailable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent lookups and conversation context may be confidential and are sent through remote API calls. <br>
Mitigation: Review confidentiality requirements before use, configure the LinkFox API key only in approved environments, and avoid submitting sensitive patent identifiers unless the service is authorized for that data. <br>
Risk: Full API responses are persistently stored locally by default and cached for 24 hours unless caching is disabled. <br>
Mitigation: Run the skill in an approved workspace, inspect or clean the generated linkfox data and cache directories when needed, and use the no-cache option for lookups that should not be reused. <br>
Risk: The skill may submit feedback to a separate service when results, user intent, or user sentiment indicate feedback is appropriate. <br>
Mitigation: Constrain or review feedback behavior before deployment when user comments, patent lookups, or API usage details may be sensitive. <br>
Risk: Patent-claim lookups consume credits and batch requests can consume a large number of credits. <br>
Mitigation: Confirm cost-sensitive requests with the user before large or repeated lookups, especially when querying many patents or retrying after empty results. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-claim-data-translated) <br>
- [Publisher profile](https://clawhub.ai/user/linkfox-ai) <br>
- [API reference](references/api.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API or script output; full responses are saved as JSON files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports patentId or patentNumber input, language selection for en/cn/jp, optional related-family substitution, 24-hour local caching unless disabled, and summarized stdout for responses over 8 KB.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
