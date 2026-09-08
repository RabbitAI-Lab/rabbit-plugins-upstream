## Description:

Generates standardized, traceable Excel test cases for industrial and collaborative robot requirements, grouped by robot module with priority coloring and coverage statistics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers, QA engineers, and robotics test engineers use this skill to convert robot requirement documents or requirement descriptions into structured Excel test-case workbooks for industrial and collaborative robots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The trigger wording is broad enough that an agent could invoke the skill for general robotics discussion or troubleshooting.

Mitigation: Invoke it explicitly for robotics test-case generation and use another skill or normal dialogue for general robotics analysis.

Risk: Generated robot test cases may be used in safety-sensitive validation workflows if accepted without review.

Mitigation: Have robotics and safety reviewers check requirements traceability, standard coverage, and test conditions before applying generated cases to physical or collaborative robots.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/robot-testcase-generator)
- [Agent Skills standard](https://agentskills.io)
- [Agent Skills reference validator](https://github.com/agentskills/agentskills/tree/main/skills-ref)
- [Robot domain knowledge](references/domain-knowledge.md)
- [Robot test case format specification](references/format-spec.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Excel workbook plus structured JSON or Markdown planning artifacts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Excel output is written locally under output/ and uses a fixed two-sheet workbook structure for test cases and coverage statistics.]

## Skill Version(s):

1.2.0 (source: server release metadata and SKILL.md frontmatter V1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
