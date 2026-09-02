## Description:

Generates standardized, traceable industrial automation test cases for PLC, SCADA, and HMI application-layer requirements and writes them to a structured Excel workbook.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, QA engineers, and industrial automation teams use this skill to convert requirements or requirement documents into import-ready Excel test cases with module grouping, priority styling, traceability, and coverage statistics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Input requirements may contain proprietary plant, device, or security details that can be carried into generated workbooks.

Mitigation: Review and sanitize generated Excel files before sharing them outside the intended project team.

Risk: Generated industrial test cases may omit context-specific safety, compliance, or site acceptance requirements.

Mitigation: Validate the workbook against source requirements, applicable industrial standards, and site procedures before using it for execution or acceptance.

Risk: The skill writes local Excel output and depends on Python 3 with openpyxl.

Mitigation: Run it in the intended workspace with reviewed dependencies and inspect the local output/ files before distribution.

## Reference(s):

- [Industrial Domain Knowledge](artifact/references/domain-knowledge.md)
- [Industrial Test Case Format Specification](artifact/references/format-spec.md)
- [Example Requirements](artifact/examples/requirements.md)
- [Agent Skills Standard](https://agentskills.io)
- [Agent Skills Reference Validator](https://github.com/agentskills/agentskills/tree/main/skills-ref)
- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/industrial-testcase-generator)

## Skill Output:

**Output Type(s):** [Files, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Excel workbook (.xlsx) with two sheets, plus structured intermediate JSON or Markdown guidance when needed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3 and openpyxl; generated workbooks are saved locally under output/ with module grouping, priority colors, and coverage statistics.]

## Skill Version(s):

1.2.0 (source: server release metadata and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
