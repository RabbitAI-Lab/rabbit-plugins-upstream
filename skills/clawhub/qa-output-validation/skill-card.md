## Description:

Checks generated test cases before final output by validating factual grounding, internal consistency, executability, and traceability back to stated requirements.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, QA engineers, and testing teams use this skill as a final quality gate for AI-generated test cases. It produces a validation report that flags hallucinated requirements, contradictory cases, unclear steps, and missing traceability before test cases are delivered.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation phrases may route general output-quality requests to this skill when stricter workflow routing is desired.

Mitigation: Use explicit activation wording or routing rules when teams need this skill to run only at the final test-case validation stage.

Risk: Validation findings can recommend marking or removing hallucinated test cases, which could affect useful work if source evidence is incomplete.

Mitigation: Confirm each flagged item against the requirement source and preserve the original test-case data before making removals or corrections.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-output-validation)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown validation report with pass/fail status, check summaries, issue tables, and traceability notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports issues against existing test case IDs and does not create new unique identifiers.]

## Skill Version(s):

1.7.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
