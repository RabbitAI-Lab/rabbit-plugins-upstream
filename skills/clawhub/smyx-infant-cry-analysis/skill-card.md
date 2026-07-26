## Description: <br>
Detects baby cries via audio AI in real time, analyzes likely causes, and identifies needs such as hunger, tiredness, pain, discomfort, or irritability to assist new parents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents assisting caregivers use this skill to analyze baby cry audio or video from local files or URLs, return structured observations about likely needs, and retrieve prior cloud analysis reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Infant audio, video, local files, or media URLs may be sent to the Life Emergence cloud service for analysis. <br>
Mitigation: Use the skill only when cloud processing of the submitted media is acceptable, and avoid submitting sensitive media unless that processing is approved. <br>
Risk: The skill can create or reuse a local service identity and persist identity material, tokens, reports, or workspace data across sessions. <br>
Mitigation: Review and delete the workspace data database and smyx-api-key.txt identity material when reports or tokens should not persist. <br>
Risk: Baby cry analysis is parenting support and may be incorrect or incomplete for health-related concerns. <br>
Mitigation: Treat outputs as reference guidance and seek medical care when crying persists or the baby appears ill, injured, or uncomfortable. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-infant-cry-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [Infant cry analysis API documentation](references/api_doc.md) <br>
- [Common analysis API error documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON] <br>
**Output Format:** [Markdown reports or JSON responses summarizing cloud-backed infant cry analysis and history queries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include recognition results, parenting suggestions, report links, and Markdown tables for historical reports.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter says 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
