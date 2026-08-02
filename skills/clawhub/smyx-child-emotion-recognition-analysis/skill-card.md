## Description: <br>
Identifies negative emotions such as crying, anger, fear, and distress through surveillance footage, issues soothing reminders, and notifies parents or caregivers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External caregivers, educators, and operators use this skill to analyze child surveillance images or videos for negative emotion signals, review structured reports, and query historical reports. Results are advisory and should not replace adult supervision or emergency response. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive child surveillance images, videos, report metadata, and identity-linked requests are sent to configured remote services. <br>
Mitigation: Use only with appropriate consent and authorization, test with non-sensitive media first, and avoid broad private file paths. <br>
Risk: The skill silently manages persistent identity tokens and local identity state with limited user-facing disclosure. <br>
Mitigation: Review local data storage after use or before uninstalling, and remove saved tokens or default identity records when they are no longer needed. <br>
Risk: Emotion analysis results may be incomplete or misleading if treated as a substitute for direct care. <br>
Mitigation: Treat outputs as advisory signals, keep adult supervision in place, and escalate urgent situations through appropriate real-world response. <br>


## Reference(s): <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-child-emotion-recognition-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON-like structured analysis reports, with optional saved text output files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports local image or video paths, remote media URLs, basic/standard/json detail modes, and cloud-backed historical report lists.] <br>

## Skill Version(s): <br>
1.0.17 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
