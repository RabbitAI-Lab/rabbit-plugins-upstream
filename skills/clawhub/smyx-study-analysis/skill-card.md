## Description: <br>
Analyzes child or student study-session images and videos to identify focus, posture, study habit, and risk signals, then returns structured reports and family education suggestions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and caregivers use this skill through an agent to submit local or URL-based study-session media, receive behavior analysis, and query cloud-stored historical reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive child or student media and identifiers are sent to remote cloud services for analysis. <br>
Mitigation: Use only media the user is authorized to process, verify the service's privacy, retention, and account controls before use, and avoid highly sensitive videos when those controls are insufficient. <br>
Risk: The skill silently creates or reuses account identity and stores service tokens in the workspace data directory. <br>
Mitigation: Treat the workspace data directory as sensitive, restrict access to it, and remove stored tokens or identity records when the skill is no longer needed. <br>
Risk: Historical report queries retrieve cloud-stored records linked to the current identity. <br>
Mitigation: Confirm the active identity and workspace before querying reports, and avoid sharing report output or report links with unauthorized users. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-study-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON analysis reports with report links and optional shell command examples.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save report output to a local file when --output is supplied; accepts local mp4/avi/mov files up to 10 MB or a public video URL.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release evidence; artifact frontmatter says 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
