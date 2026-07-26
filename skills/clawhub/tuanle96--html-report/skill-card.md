## Description: <br>
Html Report helps agents produce polished, self-contained HTML reports for analyses, audits, RCAs, reviews, summaries, and other shareable write-ups. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tuanle96](https://clawhub.ai/user/tuanle96) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and reviewers use this skill when an agent needs to turn findings, investigations, audits, or summaries into a consistent standalone HTML report that can be opened locally, shared, or attached to a pull request. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated HTML reports are designed to be easy to share and may expose sensitive content if secrets, credentials, customer PII, or confidential investigation details are included. <br>
Mitigation: Review report content before sharing and exclude secrets, tokens, credentials, customer PII, and other sensitive data from generated reports. <br>
Risk: The helper writes report files locally and may open the resulting HTML file in a browser. <br>
Mitigation: Use the intended reports directory, inspect generated files before relying on them, and run the helper with its no-open option in non-interactive or CI environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tuanle96/skills/html-report) <br>


## Skill Output: <br>
**Output Type(s):** [code, shell commands, guidance] <br>
**Output Format:** [Self-contained HTML with inlined CSS, plus Markdown guidance and bash command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes report files under plans/reports and can open the generated report in a browser.] <br>

## Skill Version(s): <br>
0.13.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
