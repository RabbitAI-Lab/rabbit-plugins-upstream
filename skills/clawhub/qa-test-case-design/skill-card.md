## Description: <br>
Transforms completed QA analysis inputs into structured, prioritized, traceable test case designs with coverage notes and review guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers, developers, and test leads use this skill after requirements, scenario, boundary, or combination analysis to turn those inputs into P0-P3 test case sets with traceability, coverage summaries, and review-ready expected results. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger phrases may activate the skill before enough upstream QA analysis is available. <br>
Mitigation: Provide clear requirements and, when possible, completed scenario, boundary, or combination analysis before using the generated case design. <br>
Risk: Generated test cases can miss product-specific details or include assumptions that do not match the target system. <br>
Mitigation: Have a QA owner review the cases, fill in system-specific test steps, and verify traceability and coverage before execution. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/kokxi/skills/qa-test-case-design) <br>
- [Coverage and Quality Standards](references/coverage-and-quality.md) <br>
- [Design Methods Reference](references/design-methods.md) <br>
- [Output Template](references/output-template-full.md) <br>
- [Review Standards](references/review-standards.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown reports and tables with structured test case fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Leaves test steps for the user to complete and emphasizes requirement-based design rather than code inspection.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
