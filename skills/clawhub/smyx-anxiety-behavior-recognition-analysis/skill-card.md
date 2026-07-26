## Description: <br>
Analyzes fixed-camera home or office videos to identify anxiety-related hand rubbing, nail biting, and pacing behaviors, then reports behavior counts, durations, trends, and non-diagnostic self-care guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, counselors, and health-application developers use this skill to turn fixed-camera video into structured behavior statistics and trend reports for anxiety self-awareness support. It should not be used to diagnose anxiety disorders, score clinical scales, or provide treatment instructions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive home or office video and anxiety-behavior results may be sent to the publisher's cloud service. <br>
Mitigation: Use only with clear informed consent, verify the publisher's retention and deletion terms, and avoid inputs that include people who have not agreed to analysis. <br>
Risk: Persistent identity, token caching, and report history can link behavioral results to an account over time. <br>
Mitigation: Confirm how accounts, tokens, and stored reports can be inspected or removed before deployment, especially on shared systems. <br>
Risk: Behavior indicators can be mistaken for a mental-health diagnosis or clinical score. <br>
Mitigation: Present outputs as visual behavior statistics and self-awareness guidance only, and route clinical concerns to qualified professionals. <br>
Risk: Normal activities such as warming hands, eating, or walking around a room may be misclassified as anxiety-related behavior. <br>
Mitigation: Review results in context, prefer longer observation windows and baseline comparisons, and avoid automated high-severity alerts from brief events. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-anxiety-behavior-recognition-analysis) <br>
- [API Documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown summaries and JSON report data from command-line analysis workflows] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports may include event counts, durations, anxiety-behavior index values, baseline comparisons, self-care suggestions, and report links; outputs are behavioral indicators, not medical diagnoses.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
