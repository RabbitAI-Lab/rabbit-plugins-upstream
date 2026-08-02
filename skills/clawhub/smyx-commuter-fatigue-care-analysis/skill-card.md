## Description: <br>
Analyzes authorized smart-home living-room video or URL inputs for after-work fatigue cues and returns a fatigue report with care actions such as gentle speaker messages, soothing music, and warm lighting. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and smart-home developers use this skill to analyze authorized after-work living-room media for fatigue cues, receive structured fatigue scores and care recommendations, and query cloud-stored history reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive home video, audio, or URL inputs may be sent to a cloud backend for fatigue analysis. <br>
Mitigation: Use the skill only with authorized media, obtain clear consent from recorded people, and enforce retention controls before deployment. <br>
Risk: The skill can create a persistent local identity and store service tokens in workspace data. <br>
Mitigation: Protect the workspace data store, restrict file access, and review token handling before installing or running the skill. <br>
Risk: Fatigue scores and care actions can be mistaken or treated as health conclusions. <br>
Mitigation: Present outputs as non-diagnostic wellness guidance, keep interventions optional and rate-limited, and preserve user controls to pause or opt out. <br>


## Reference(s): <br>
- [API documentation](references/api_doc.md) <br>
- [ClawHub skill release page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-commuter-fatigue-care-analysis) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown or JSON analysis report with fatigue signals, recommended care actions, history tables, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts local media paths or network URLs; can save output to a file or list cloud history reports.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata; artifact frontmatter reports 1.0.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
