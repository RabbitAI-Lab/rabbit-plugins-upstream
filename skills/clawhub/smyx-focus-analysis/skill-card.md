## Description: <br>
Analyzes video or image inputs for gaze direction, head pose, facial landmarks, focus level, distraction, and mind-wandering indicators, then returns a structured concentration report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers can use this skill to submit classroom, office, or driving attention media for focus analysis and to retrieve prior cloud-hosted analysis reports. The skill is suited to generating structured attention summaries, trend data, suggestions, and report links for human review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive face or attention media may be uploaded to the publisher's cloud service for analysis. <br>
Mitigation: Use only media that users are authorized to process, confirm consent for identifiable people, and review the service destination and retention expectations before deployment. <br>
Risk: Analysis history is linked to an automatically managed account identity with locally stored tokens. <br>
Mitigation: Review token storage expectations, restrict runtime access to the skill workspace, and clear local account state when the skill is no longer needed. <br>
Risk: Focus and distraction results can affect decisions about students, employees, drivers, or other identifiable people. <br>
Mitigation: Treat outputs as decision-support information only and require human review before using results in operational, educational, employment, or safety decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-focus-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, files] <br>
**Output Format:** [Markdown or JSON text with optional saved output file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include focus scores, trend data, distraction counts, suggestions, historical report records, and report export links.] <br>

## Skill Version(s): <br>
1.0.8 (source: server release evidence; artifact frontmatter reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
