## Description:

Generates structured, traceable automotive electronics test cases from requirements and prepares Excel-ready outputs grouped by vehicle module.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

Apache-2.0

## Use Case:

Developers and automotive QA engineers use this skill to convert vehicle requirement documents or requirement descriptions into module-grouped test cases, coverage statistics, and Excel workbooks for HIL, bench, CANoe, and validation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may process private automotive engineering requirements while generating test cases and Excel files.

Mitigation: Provide only requirements intended for this workflow and review generated outputs before sharing them outside the authorized project team.

Risk: Generated automotive validation content can misinterpret requirements or miss applicable safety, security, or standards obligations.

Mitigation: Review generated cases against source requirements, applicable OEM and industry standards, and execution evidence before using them for release decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/automotive-testcase-generator)
- [Automotive domain knowledge](references/domain-knowledge.md)
- [Automotive test-case format specification](references/format-spec.md)
- [Example automotive requirements](examples/requirements.md)
- [Agent Skills standard](https://agentskills.io)
- [Agent Skills reference validation](https://github.com/agentskills/agentskills/tree/main/skills-ref)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Files]

**Output Format:** [Markdown analysis, JSON test-case structures, and Python-generated .xlsx files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Python 3 and openpyxl for Excel output; writes local workbooks under output/.]

## Skill Version(s):

1.1.0 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
