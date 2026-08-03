## Description: <br>
AI-powered flowering-date prediction for ornamental and cut-flower plants using bud images or videos, optional temperature and light data, and a pre-trained phenology model to estimate full bloom dates within the next 3-7 days. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External growers, greenhouse operators, botanical garden teams, and agricultural developers use this skill to analyze flower-bud media and produce bloom-date predictions, confidence information, phenology-stage observations, and production-planning guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends images, videos, URLs, report history requests, and account-linked identifiers to lifeemergence.com services. <br>
Mitigation: Install and run only where sending this media and report metadata to the remote service is acceptable. <br>
Risk: The skill can automatically create or reuse a local identity and persist remote-service tokens with limited user control. <br>
Mitigation: Review and clear the workspace data directory and SQLite token storage when persistent identity reuse is not desired. <br>
Risk: Flowering-date predictions are planning aids and may be inaccurate for final production scheduling. <br>
Mitigation: Use predictions alongside manual crop inspection, historical grower experience, and local environmental observations. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-flowering-date-prediction-analysis) <br>
- [Publisher profile](https://clawhub.ai/user/18072937735) <br>
- [Skill demo](https://lifeemergence.com/sample.html) <br>
- [API documentation](references/api_doc.md) <br>
- [Analysis API documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown and JSON-style structured analysis reports with optional saved output files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include report links and historical-report tables returned by remote lifeemergence.com services.] <br>

## Skill Version(s): <br>
1.0.5 (source: server release evidence; artifact frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
