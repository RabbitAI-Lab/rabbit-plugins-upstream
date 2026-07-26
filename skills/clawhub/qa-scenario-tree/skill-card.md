## Description: <br>
Helps QA practitioners turn decomposed requirements into structured scenario trees covering happy paths, alternative paths, exception paths, business rules, and data-flow scenarios. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers, developers, and product teams use this skill after requirements decomposition to design scenario coverage for complex workflows with page transitions, state changes, branching behavior, and exception handling. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Example QA inputs may include customer, payment, identity, screenshot, or production data. <br>
Mitigation: Mask or remove sensitive data before using the skill, and use synthetic or sanitized test examples whenever possible. <br>
Risk: Scenario trees can miss branches or grow too large for practical test planning. <br>
Mitigation: Review generated scenarios against the requirements decomposition, prioritize critical P0-P1 branches, and reclassify misplaced happy-path, alternative-path, exception-path, and data-flow scenarios. <br>


## Reference(s): <br>
- [Qa Scenario Tree on ClawHub](https://clawhub.ai/kokxi/skills/qa-scenario-tree) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with structured scenario IDs, requirement links, path categories, expected results, data changes, and risk levels.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scenario outputs use SC-XXXX identifiers, link back to REQ-XXXX requirements, and separate happy-path, alternative-path, exception-path, and data-flow coverage.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
