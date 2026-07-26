## Description: <br>
Identifies infant sleep states such as deep sleep, light sleep, waking, and restlessness, then generates structured sleep reports and schedule analysis. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to analyze baby sleep monitoring video or image inputs, classify sleep states, summarize sleep timing and awakenings, and retrieve prior cloud reports. Results are for parenting reference and are not a substitute for professional medical advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Baby-monitoring media, media URLs, and identifiers are processed by a cloud service. <br>
Mitigation: Use only when the publisher's privacy and retention practices are acceptable, and avoid submitting unrelated or highly sensitive media. <br>
Risk: The skill may automatically create or reuse account identity and store authentication tokens in the workspace data directory. <br>
Mitigation: Run in a controlled workspace, protect or clear stored tokens according to local policy, and avoid sharing the workspace with untrusted users. <br>
Risk: Cloud report history can be queried by the skill. <br>
Mitigation: Use history retrieval only when the user expects prior report access and the account context is appropriate. <br>


## Reference(s): <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands] <br>
**Output Format:** [Markdown text with JSON analysis content, history lists, and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write an optional output file when requested; supports mp4, avi, and mov inputs up to 10 MB.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence; packaged SKILL.md frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
