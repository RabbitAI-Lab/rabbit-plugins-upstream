## Description: <br>
AI-powered pet sleep quality analysis from a fixed bed/rest-area camera that distinguishes sleep and wake states, totals sleep duration, counts roll-overs and startle awakenings, and returns a 0-100 sleep-quality score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, pet owners, animal hospitals, and pet boarding operators use this skill to analyze pet rest-area video for sleep duration, roll-over count, startle awakenings, and sleep-quality scoring. The output is for sleep-health reference and is not a medical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pet or home video may be processed by a remote service. <br>
Mitigation: Use only footage that the user is willing and authorized to upload, and avoid videos that reveal sensitive people, rooms, or locations. <br>
Risk: The skill can automatically associate work with a cloud-linked identity and store service tokens locally. <br>
Mitigation: Run it only under the intended account context, isolate the execution environment when reviewing it, and remove local credential or database artifacts after use if retention is not desired. <br>
Risk: Cloud history lookup may return reports associated with the current account context. <br>
Mitigation: Confirm the account context before listing reports and share history output only with users authorized to see those reports. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-sleep-quality-analysis-analysis) <br>
- [Publisher Profile](https://clawhub.ai/user/18072937735) <br>
- [Pet Sleep Quality Analysis API Documentation](artifact/references/api_doc.md) <br>
- [Shared Analysis API Documentation](artifact/skills/smyx_analysis/references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files] <br>
**Output Format:** [Markdown or JSON analysis report with optional saved result file and report export link.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include cloud-backed history-list results and report image/export URLs.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release metadata; artifact frontmatter reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
