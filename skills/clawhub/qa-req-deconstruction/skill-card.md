## Description: <br>
Qa Req Deconstruction breaks vague requirement descriptions into testable input, operation, state, output, and rule dimensions while surfacing implicit and derived requirements. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
QA engineers, developers, and product teams use this skill to turn PRDs, URLs, file paths, or short requirement descriptions into structured requirement IDs, explicit requirements, implicit requirements, derived requirements, business rules, five-dimension breakdowns, risks, and open questions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Requirement inputs may contain production data, customer information, payment details, or identity data. <br>
Mitigation: Redact or mask sensitive data before using the skill, and prefer sanitized requirement examples. <br>
Risk: Broad trigger wording may activate the skill for general requirement-analysis requests. <br>
Mitigation: Confirm the user wants QA-focused requirements decomposition before applying the workflow. <br>
Risk: Implicit or derived requirements can be mistaken for confirmed product requirements. <br>
Mitigation: Label inferred items as assumptions or pending confirmation and review them with product or QA owners. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Structured Markdown requirement decomposition tables and checklists] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes requirement IDs, risk IDs, five-dimension breakdowns, and assumption labels.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
