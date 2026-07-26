## Description: <br>
Retrieves translated patent titles and abstracts from Zhihuiya (PatSnap) for a single patent in Chinese, English, or Japanese. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Patent researchers, IP teams, and agent users use this skill to retrieve translated titles and abstracts for one known patent by patent ID or publication number. It helps present PatSnap abstract data clearly without adding patent interpretation or legal analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a credentialed LinkFox/PatSnap API and can send patent or work-product identifiers and requests to the configured gateway. <br>
Mitigation: Review or restrict LINKFOX_TOOL_GATEWAY, confirm LinkFox credential use is approved, and avoid sensitive patent data unless external processing is acceptable. <br>
Risk: The skill stores full API responses locally, including cached and session data. <br>
Mitigation: Review generated linkfox data/cache files, protect the workspace appropriately, and delete stored responses when they are no longer needed. <br>
Risk: Security evidence notes feedback reporting and possible onboarding-skill installation behavior that users should review before installation. <br>
Mitigation: Review prompts before reporting feedback or installing additional skills, and require explicit user authorization for downloads or onboarding steps. <br>


## Reference(s): <br>
- [智慧芽摘要翻译 API 参考](references/api.md) <br>
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-abstract-data-translated) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown tables, explanatory text, shell command guidance, and JSON API responses or summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LinkFox API credentials; full API responses are stored in local linkfox data/cache files and large responses may be summarized on stdout.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
