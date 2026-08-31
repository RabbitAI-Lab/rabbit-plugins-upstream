## Description:

Generates standardized, traceable robot and ROS test cases from requirements documents or requirement descriptions, then organizes them into structured Excel workbooks by robot module.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and robotics test teams use this skill to turn robot, industrial robot, service robot, mobile robot, and ROS requirements into structured test cases. It is intended for test design and workbook generation, not automated test script generation or test execution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated test cases may be incomplete, incorrect, or misaligned with the user's actual robot requirements and applicable safety standards.

Mitigation: Review the generated workbook against the source requirements, standards, and safety acceptance criteria before importing it into a test management system or using it for release decisions.

Risk: The skill processes user-provided requirement documents that may contain sensitive project or product information.

Mitigation: Use only approved input documents for the execution environment and review generated Excel files before sharing them outside the intended team.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/robot-testcase-generator)
- [Robot Domain Knowledge](references/domain-knowledge.md)
- [Robot Test Case Format Specification](references/format-spec.md)
- [Example Robot Requirements](examples/requirements.md)
- [Agent Skills Standard](https://agentskills.io)
- [Agent Skills Reference Validation](https://github.com/agentskills/agentskills/tree/main/skills-ref)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Files]

**Output Format:** [Markdown guidance and Python/openpyxl-generated Excel workbooks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates a two-sheet .xlsx workbook with test cases and coverage statistics; requires Python 3 and openpyxl.]

## Skill Version(s):

1.1.0 (source: server release metadata; artifact frontmatter V1.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
