## Description:

Reviews AI-generated test cases before final release by sampling and checking business validity, scenario completeness, and executability, then requiring closure on any systemic issues found.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kokxi](https://clawhub.ai/user/kokxi)

### License/Terms of Use:

MIT-0

## Use Case:

QA engineers, test leads, and development teams use this skill to perform final expert review of AI-generated test cases before release. It produces review findings, corrections, learning points, and prompt optimization feedback for improving future test generation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad trigger phrases could cause the QA review template to be used for general document checking instead of final test-case review.

Mitigation: Invoke the skill explicitly for final review of AI-generated test cases after output critique and blindspot compensation.

Risk: Expert review findings can affect release readiness if systemic coverage or executability issues are found.

Mitigation: Route systemic issues back through correction, record them as prompt optimization feedback, and re-run sampling before treating the test set as release-ready.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kokxi/skills/qa-expert-review)

## Skill Output:

**Output Type(s):** [Markdown, Analysis, Guidance]

**Output Format:** [Markdown report with tables, issue lists, corrections, learning points, and prompt optimization suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a unique review ID, sampling rate, traceable test case identifiers, severity-style correction markers, and coverage statements tied to the provided requirements or input documents.]

## Skill Version(s):

1.7.5 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
