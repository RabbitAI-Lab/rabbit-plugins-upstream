## Description: <br>
Produces audience-specific QA test reports, including daily updates, weekly summaries, iteration reports, and quality decision summaries with metrics, risks, traceability IDs, and recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers, test leads, project managers, and management stakeholders use this skill to turn test execution data, defect data, and optional quality metrics into reports tailored to the reader's decision needs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may trigger on generic requests such as daily report or progress report. <br>
Mitigation: Specify that the requested report is for QA/testing, or choose a general project reporting workflow when the report is not test-related. <br>
Risk: Report fields such as release recommendation or delay recommendation may be mistaken for an approved operational decision. <br>
Mitigation: Treat release and delay recommendations as report content for stakeholder review, and require authorized human approval before acting on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-test-reporting) <br>
- [Publisher profile](https://clawhub.ai/user/kokxi) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown reports and structured report guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports include a unique report ID and aggregate related use case, defect, and requirement IDs when available.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
