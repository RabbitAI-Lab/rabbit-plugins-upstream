## Description: <br>
Retrieves patent description/specification data from the Zhihuiya patent database for a single patent ID or publication number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to retrieve full patent description text from LinkFox/Zhihuiya services when a user supplies a single patent ID or publication number. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent identifiers and retrieved descriptions are sent to LinkFox/Zhihuiya services. <br>
Mitigation: Install and use only when that data sharing is acceptable for the patents being queried. <br>
Risk: Full API responses are saved locally and may persist beyond the immediate task. <br>
Mitigation: Review the saved linkfox data location and delete stored responses when they are no longer needed. <br>
Risk: The skill can report interaction feedback through a separate LinkFox endpoint. <br>
Mitigation: Review feedback behavior before use and avoid sending sensitive user details in feedback content. <br>
Risk: Queries may consume paid LinkFox/Zhihuiya credits. <br>
Mitigation: Confirm credit consumption before running lookups, especially when users request multiple patents. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-description-data) <br>
- [Zhihuiya patent description API reference](references/api.md) <br>
- [LinkFox API key and credit guide](https://skill.linkfox.com/linkfoxskills/guide.htm) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, shell commands, JSON API responses, and saved JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts one patentId or patentNumber per request, plus optional replaceByRelated; large responses are saved locally and summarized unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
