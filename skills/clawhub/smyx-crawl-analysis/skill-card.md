## Description: <br>
Analyzes reptile and arachnid pet videos or URLs with a cloud API to return structured health findings, care suggestions, historical report data, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit reptile or arachnid pet media for cloud health analysis, receive structured findings and care suggestions, and retrieve prior cloud reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Cloud-backed analysis uploads media files or submits remote URLs outside the local environment. <br>
Mitigation: Use only media and URLs appropriate for the publisher's cloud service, and avoid sensitive media or private/internal URLs unless that data handling is acceptable. <br>
Risk: The workflow can create or reuse an internal identity, store tokens, and list prior cloud reports. <br>
Mitigation: Review account, token, and report-history behavior before deployment, and run it only where cloud-linked history access is expected. <br>
Risk: The artifact includes camera-monitoring commands outside the core health-analysis flow. <br>
Mitigation: Avoid monitoring commands unless camera use has been explicitly reviewed and approved for the deployment. <br>
Risk: Health findings are advisory and may be incorrect or incomplete. <br>
Mitigation: Treat reports as reference information and consult a qualified veterinarian for diagnosis or treatment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crawl-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Files, Guidance] <br>
**Output Format:** [Markdown text with structured JSON sections and report links; optional saved output file.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud report export links and historical report lists.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
