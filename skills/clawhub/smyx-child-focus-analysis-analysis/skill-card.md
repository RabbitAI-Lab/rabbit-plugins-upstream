## Description: <br>
Analyzes child study-area video or video URLs to report visual focus indicators, per-minute focus scores, distraction periods, and historical report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, parents, teachers, and developers use this skill to analyze child study-area media for focus scores, distraction-event statistics, structured reports, and cloud report history. Results are visual behavior indicators and should support, not replace, guardian or teacher judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive child study-area media may be uploaded to the vendor's cloud service for analysis. <br>
Mitigation: Use only with guardian consent, avoid private or signed media URLs, and submit the minimum necessary media for the analysis task. <br>
Risk: Reports can be associated with a persistent local or remote identity and identity tokens may remain in workspace data. <br>
Mitigation: Review and delete the workspace data database and smyx-api-key.txt when the skill is no longer needed or when rotating users. <br>
Risk: Focus scores and distraction labels can be mistaken for definitive educational or behavioral assessment. <br>
Mitigation: Treat outputs as visual behavior indicators and verify conclusions with a parent, guardian, or teacher before acting on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-child-focus-analysis-analysis) <br>
- [API documentation](references/api_doc.md) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, JSON, Files, API Calls, Guidance] <br>
**Output Format:** [Markdown and JSON-like structured text, with optional file output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links, historical report records, focus scores, distraction events, and exported report image URLs.] <br>

## Skill Version(s): <br>
1.0.7 (source: ClawHub release metadata; artifact frontmatter reports 1.0.9) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
