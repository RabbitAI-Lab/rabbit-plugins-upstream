## Description: <br>
Analyzes face image or video inputs to produce psychological stress, anxiety tendency, and depression tendency assessment reports for mental health monitoring scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit face media for psychological stress assessment, receive structured results, and retrieve prior cloud-hosted reports. It is suited to mental health monitoring workflows where users understand that the assessment is informational and not a clinical diagnosis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face media and psychological-stress inferences may be sent to a remote service and later retrieved as cloud history. <br>
Mitigation: Use only with explicit user understanding and approved media; clarify retention, retrieval, and deletion expectations before use. <br>
Risk: Reports may be linked to an internal identity and reusable local tokens. <br>
Mitigation: Avoid shared workspaces unless identity isolation is in place, and review token storage and account-scoping practices before deployment. <br>
Risk: Stress, anxiety, and depression tendency outputs may be mistaken for clinical diagnosis. <br>
Mitigation: Present results as informational mental health assessment references and direct users with persistent concerns to qualified professionals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-psychological-stress-assessment-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API interface documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, files, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with optional saved output file and report link] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include stress index, anxiety tendency, depression tendency, suggestions, history tables, and exported report URLs.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence; artifact frontmatter reports 1.0.12) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
