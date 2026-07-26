## Description: <br>
Checks whether a QA testing request includes a clear requirement, enough context, and usable supporting inputs before downstream test design begins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kokxi](https://clawhub.ai/user/kokxi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, QA engineers, and test designers use this skill at the start of a testing workflow to assess whether a user's request has enough requirement detail, context, and readable attachments or URLs. When information is missing, it returns the gaps and clarification questions needed before continuing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Sensitive customer, payment, identity, financial, or production data may be disclosed if submitted in prompts, files, screenshots, or requirement links. <br>
Mitigation: Sanitize or mask sensitive data before use, and avoid providing real production records unless they have been reviewed for sharing. <br>
Risk: Incomplete or ambiguous requests can still produce minimal test ideas or misleading downstream assumptions. <br>
Mitigation: Review the validation result, missing information list, and clarification questions before using the output to drive test design. <br>
Risk: The skill may read provided workspace files or fetch user-supplied requirement links as part of validation. <br>
Mitigation: Provide only files and URLs intended for review, and confirm access requirements before relying on URL-based content. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-input-validation) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with structured validation fields] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes validation_result, input_quality_score, missing_info, clarification_questions, and recommendation; the skill states that it does not generate a unique traceability ID.] <br>

## Skill Version(s): <br>
1.6.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
