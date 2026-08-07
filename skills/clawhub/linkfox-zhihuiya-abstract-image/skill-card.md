## Description: <br>
Retrieves patent abstract drawings from the Zhihuiya patent database by patent ID or publication number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to retrieve representative patent abstract drawings from Zhihuiya/PatSnap by patent ID or publication number, including batch lookups of up to 100 patents. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent identifiers, API credentials, and session metadata are sent to LinkFox services during lookup. <br>
Mitigation: Use the skill only for workflows where sharing those values with LinkFox is acceptable, and keep API keys scoped and rotated according to local policy. <br>
Risk: Full API responses are saved in the local workspace and may include patent lookup data. <br>
Mitigation: Use a controlled workspace for sensitive work and delete saved response files when retention is not needed. <br>
Risk: The skill includes automatic feedback reporting and guidance to install an external onboarding skill. <br>
Mitigation: Review feedback behavior and any external skill installation before enabling them in confidential or managed environments. <br>


## Reference(s): <br>
- [智慧芽-摘要附图 API Reference](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-abstract-image) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Files, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with patent image links and JSON response files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Saves full API responses locally, prints full JSON for small responses, and prints a summary for larger responses unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
