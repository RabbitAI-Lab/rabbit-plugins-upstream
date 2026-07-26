## Description: <br>
抖音账号诊断宗师 uses the RedFox API to analyze a Douyin account by name or ID and generate a four-dimension performance diagnosis with scoring details and optimization guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[redfox-data](https://clawhub.ai/user/redfox-data) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External brand teams, MCN operators, Douyin creators, and content operators use this skill to evaluate Douyin account health, partnership fit, recent content performance, and practical account optimization actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Douyin account names or IDs are sent to RedFox for diagnosis and may be submitted for collection when an account is not found. <br>
Mitigation: Use explicit diagnosis requests and confirm with the user before submitting an unlisted account for collection. <br>
Risk: A RedFox API key is required and could be exposed if copied into prompts, code, logs, or output files. <br>
Mitigation: Configure REDFOX_API_KEY through the environment and avoid hard-coding or printing the full key. <br>
Risk: Fallback web search can produce less authoritative account data than the RedFox API. <br>
Mitigation: Treat RedFox API data as authoritative, label any fallback source clearly, and do not estimate missing API fields. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/redfox-data/skills/douyin-account-diagnosis-redfox) <br>
- [Core workflow reference](references/core_workflow.md) <br>
- [RedFoxHub](https://redfox.hk) <br>
- [RedFox API key settings](https://redfox.hk/settings/api-keys?source=clawhub) <br>
- [RedFox Douyin account query API](https://redfox.hk/story/api/dyUser/query) <br>
- [RedFox Douyin account collection API](https://redfox.hk/story/api/dyUser/syncUserNotes) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown diagnostic report with a scoring breakdown, account data tables, overall score, strengths, weaknesses, and optimization suggestions.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a Douyin account name or ID and REDFOX_API_KEY; may ask for explicit user confirmation before submitting an unlisted account for collection.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
