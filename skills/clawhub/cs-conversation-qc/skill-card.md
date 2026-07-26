## Description: <br>
客服会话质检 helps agents batch-analyze Chinese customer-service chat exports, apply configurable quality-control rules, mask sensitive data, and produce score reports with evidence and human-review items. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zenobiazizi](https://clawhub.ai/user/zenobiazizi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer-service supervisors, quality analysts, and operations teams use this skill to review Chinese support conversations, score them against configurable QC rules, and identify items that need human review before operational or employee-evaluation use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer-service chat exports can contain personal data and sensitive customer issues. <br>
Mitigation: Use the skill only for intentional QC tasks, keep processing in the local agent environment, and mask phone numbers, identity numbers, bank cards, and detailed addresses in reports. <br>
Risk: Automated QC scores may be incomplete or uncertain when conversation format, language, work schedule, or semantic judgment is ambiguous. <br>
Mitigation: Confirm unclear input structure before large runs, route low-confidence findings and unparseable conversations to review lists, and manually review the report before employee evaluation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zenobiazizi/skills/cs-conversation-qc) <br>
- [Default customer-service QC rules](references/rules-default.md) <br>
- [Custom QC rules guide](references/rules-guide.md) <br>
- [Sample QC report](examples/sample-report.md) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, files, guidance] <br>
**Output Format:** [Excel workbook when available, otherwise Markdown tables with masked evidence, QC scores, and human-review sections] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reports omit raw private data, cite only short masked evidence snippets, and separate low-confidence findings into a human-review list.] <br>

## Skill Version(s): <br>
1.0.3 (source: ClawHub server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
