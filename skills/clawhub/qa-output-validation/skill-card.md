## Description:

Validates generated QA test cases before final output by checking factual grounding, consistency, executability, and traceability to source requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test developers, and agents use this skill as a final quality gate for generated test cases before publication or handoff. It identifies hallucinated requirements, inconsistent cases, vague execution steps, and missing traceability.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Trigger phrases about output quality may activate the skill in broad QA discussions.

Mitigation: Review trigger phrases before deployment and align them with the intended workflow.

Risk: Flagged hallucinations could lead users or agents to remove or change generated test cases too quickly.

Mitigation: Confirm the source requirements and preserve the original data before removing or changing flagged cases.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-output-validation)
- [Publisher profile](https://clawhub.ai/user/kokxi)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown validation report with pass/fail status, check results, issue lists, and traceability notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces QA validation findings for generated test cases; does not create new persistent identifiers.]

## Skill Version(s):

1.7.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
