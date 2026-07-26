## Description: <br>
Chief is an HR deep organizational diagnosis skill that uses a seven-step reasoning workflow, Socratic information audit, iceberg analysis, multi-agent review, citation checking, and evaluator critique to turn ambiguous people and organization problems into structured diagnostic reports. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tuobadaidai](https://clawhub.ai/user/tuobadaidai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
HR leaders, HRBPs, organization development teams, and managers use this skill to analyze complex HR and organizational questions such as attrition, team health, leadership assessment, culture diagnosis, compensation benchmarking, change readiness, and talent review. It is not intended for routine HR requests such as simple policy lookup, template generation, or email drafting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can process sensitive HR information such as employee names, compensation, disputes, performance details, and confidential business context. <br>
Mitigation: Redact identifiers before use, restrict access to approved HR users, and run the skill only in environments cleared for sensitive employee data. <br>
Risk: The skill describes automatic case-memory and failure-taxonomy writeback, which may retain sensitive HR case details without clear opt-in or retention controls. <br>
Mitigation: Use a dedicated knowledge-base path, disable or manually control writeback, and apply organizational retention and deletion rules before deployment. <br>
Risk: Diagnostic reports and recommendations may influence employment, compensation, or organizational decisions. <br>
Mitigation: Require qualified human review before acting on findings, verify cited data sources, and document decision ownership outside the skill output. <br>


## Reference(s): <br>
- [ClawHub Chief release page](https://clawhub.ai/tuobadaidai/skills/chief) <br>
- [Skill definition](artifact/SKILL.md) <br>
- [Enhanced HR analysis frameworks](artifact/references/enhanced-frameworks.md) <br>
- [Evaluator quality specification](artifact/references/evaluator-spec.md) <br>
- [State pruning specification](artifact/references/state-pruning-spec.md) <br>
- [XML scaffold specification](artifact/references/xml-scaffold-spec.md) <br>
- [Multi-agent aggregation strategy](artifact/references/multi-agent-aggregation.md) <br>
- [Humanizer writing-pattern reference](https://github.com/blader/humanizer) <br>


## Skill Output: <br>
**Output Type(s):** [Analysis, Markdown, Guidance, Configuration, Shell commands] <br>
**Output Format:** [Markdown diagnostic reports with structured recommendations, citations, confidence labels, and optional shell commands for knowledge-base initialization or citation checks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May use XML-structured intermediate state internally and may reference a local HR knowledge base when configured.] <br>

## Skill Version(s): <br>
5.0.1 (source: server release metadata; artifact frontmatter reports 5.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
