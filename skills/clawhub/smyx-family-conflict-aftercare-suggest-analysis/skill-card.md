## Description: <br>
Analyzes household public-area audio/video to detect family conflict signals, wait for a calm window, and produce aftercare suggestions or safety escalation guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to analyze household living-room, kitchen, or dining-area audio/video for conflict events and receive structured aftercare guidance, report links, or safety-resource escalation when redline signals are present. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive household conflict audio/video or URLs may be sent to the provider's cloud service and linked to a reused or created identity. <br>
Mitigation: Use only with informed consent from recorded household members, and confirm report visibility, retention, deletion, and access controls before deployment. <br>
Risk: Stored tokens, report links, or history could expose private family conflict records. <br>
Mitigation: Protect tokens and report links, restrict history retrieval to authorized users, and document how local and cloud history can be deleted. <br>
Risk: Aftercare prompts could be harmful if triggered during an active or unsafe conflict. <br>
Mitigation: Require the calm-window and redline checks described by the artifact before triggering aftercare; route suspected violence, minors in conflict, dangerous objects, or injury signs to safety resources instead. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-family-conflict-aftercare-suggest-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [Markdown report or JSON with conflict signals, aftercare recommendations, safety resources, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include historical report tables and safety-resource escalation guidance.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata; artifact frontmatter reports 1.0.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
