## Description: <br>
Analyze Amazon keyword demand, market structure, weekly trends, observed SERP signals, and ASIN keyword visibility or traffic observations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, advertising analysts, and agent operators use this skill to perform Amazon keyword expansion, keyword deep dives, reverse-ASIN traffic-structure review, and evidence-bounded traffic-change diagnosis using ZooData-backed signals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a ZooData API key and can call ZooData services for Amazon keyword and ASIN analysis. <br>
Mitigation: Install it only when that credential and network access are acceptable, and prefer the ZOODATA_API_KEY environment variable for credential handling. <br>
Risk: The security scan reports broader web-interaction and API tooling than the core keyword-analysis task needs. <br>
Mitigation: Avoid the interactive WebTools path on logged-in or state-changing pages, and review requests that would use page actions or non-keyword CLI capabilities. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/apiclaw/skills/amazon-keyword-traffic-analysis) <br>
- [ZooData Skills Homepage](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [README](README.md) <br>
- [ZooData CLI Contract](references/cli-contract.md) <br>
- [Production API and Acquisition Reference](references/reference.md) <br>
- [Execution Guide](references/execution-guide.md) <br>
- [Evidence Protocols](references/evidence-protocols.md) <br>
- [Diagnosis Action Protocols](references/diagnosis-action-protocols.md) <br>
- [Output Rules](references/output-rules.md) <br>
- [Keyword Analysis Scenario](references/scenarios-keyword-analysis.md) <br>
- [Reverse ASIN Scenario](references/scenarios-reverse-asin.md) <br>
- [Keyword Traffic Diagnosis Scenario](references/scenarios-keyword-traffic-diagnosis.md) <br>
- [SQP Field Semantics](references/sqp-field-semantics.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown reports with concise analysis, evidence notes, and command-aware retrieval summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ZOODATA_API_KEY and uses ZooData APIs for Amazon keyword and ASIN evidence.] <br>

## Skill Version(s): <br>
0.1.5 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
