## Description: <br>
Analyzes face-focused images, videos, or media URLs for micro-expression and emotion signals, returning structured emotion reports, recommendations, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to submit face-focused media files or URLs for micro-expression emotion analysis and to retrieve historical analysis reports. Results should be treated as informational support, not as a substitute for professional psychological, legal, employment, medical, or other high-stakes judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Face videos, images, or media URLs are sent to configured cloud APIs for analysis. <br>
Mitigation: Use only media that is appropriate to share with the configured service, and obtain any required consent before processing. <br>
Risk: The skill may create or reuse a local identity and store account tokens locally. <br>
Mitigation: Run it in an isolated workspace when possible, and review or clear local workspace data if persistent identity linkage is not desired. <br>
Risk: Emotion and micro-expression results can be misleading if used as high-stakes evidence. <br>
Mitigation: Treat outputs as informational and require human review; avoid covert, employment, legal, medical, or other high-stakes judgments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-emotion-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown summaries and JSON analysis results from media analysis or report-list requests] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include analysis status, emotion findings, recommendations, historical report tables, and report links.] <br>

## Skill Version(s): <br>
1.0.11 (source: server release metadata; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
