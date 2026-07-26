## Description: <br>
Provides QA guidance for bulk test data generation, data masking, compliance-aware data handling, and test data factory design. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers, test automation developers, and data engineers use this skill to plan repeatable test data construction, masking, cleanup, lifecycle management, and traceability for test environments. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Database cleanup examples could delete real data if applied to production or shared environments. <br>
Mitigation: Use them only in isolated test environments, preview affected rows, wrap changes in transactions, require clear test-data markers, and obtain DBA approval before execution. <br>
Risk: Production-data masking guidance could be applied without confirming compliance requirements or sensitive-field coverage. <br>
Mitigation: Validate masking rules against the applicable privacy and compliance requirements before using production-derived data in tests. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-test-data-engineering) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with structured sections, checklists, and inline SQL/Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs include DATA-XXXX traceability identifiers and structured data_strategy, data_generation, data_mask_rules, and data_management sections.] <br>

## Skill Version(s): <br>
1.6.0 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
