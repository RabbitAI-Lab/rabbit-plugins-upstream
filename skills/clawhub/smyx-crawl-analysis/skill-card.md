## Description: <br>
Analyzes reptile and arachnid videos or URLs through a server-side API to identify visible health indicators and produce a Pet Safety Guardian health report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit reptile or arachnid media for cloud health analysis, retrieve structured findings, and query prior reports. Results are health references and should not replace professional veterinary diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Uploaded reptile media or provided URLs are sent to lifeemergence.com services for analysis. <br>
Mitigation: Obtain explicit user consent before uploads or URL submissions, and avoid submitting sensitive private media unless the publisher documents retention and handling practices clearly. <br>
Risk: The skill may create or reuse an internal account identity, query cloud history, and persist service tokens locally. <br>
Mitigation: Review identity, token storage, and report-history behavior before deployment; restrict workspace access and clear local data when the skill is no longer needed. <br>
Risk: The generated health report may be mistaken for a professional veterinary diagnosis. <br>
Mitigation: Present results as health references only and direct users to a qualified veterinarian for diagnosis or treatment decisions. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-crawl-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](artifact/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files] <br>
**Output Format:** [Markdown or JSON health analysis report with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports basic, standard, and JSON detail levels; local video input is limited to mp4, avi, or mov files up to 10 MB.] <br>

## Skill Version(s): <br>
1.0.9 (source: frontmatter and server release) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
