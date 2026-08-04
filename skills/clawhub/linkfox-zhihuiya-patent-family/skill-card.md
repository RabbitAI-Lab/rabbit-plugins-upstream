## Description: <br>
Queries Zhihuiya (PatSnap) patent family information by patent ID or publication number, including Simple Family, INPADOC Family, and PatSnap Family members. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, patent analysts, and developers use this skill to retrieve and summarize patent family members for known patent IDs or publication numbers, compare Simple, INPADOC, and PatSnap family scopes, and understand jurisdiction coverage without receiving legal opinions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Patent lookup results are saved locally by default. <br>
Mitigation: Review where response files are stored and handle saved patent data according to the user's data retention and confidentiality requirements. <br>
Risk: Output may be written outside the documented project path in fallback cases. <br>
Mitigation: Confirm the active workspace and output path before using saved results, especially in restricted or read-only directories. <br>
Risk: Setup guidance may install an external onboarding skill for authentication or billing issues. <br>
Mitigation: Review any onboarding skill before installation and get user authorization before downloading external setup assets. <br>
Risk: Feedback may be sent to a separate LinkFox service without a clear opt-in step. <br>
Mitigation: Avoid sending user feedback unless the user has consented and the content does not include sensitive patent or business information. <br>


## Reference(s): <br>
- [智慧芽专利家族查询 API 参考](references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-family) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown summaries with optional JSON files and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes full API responses to local JSON files and may summarize large responses in stdout.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
