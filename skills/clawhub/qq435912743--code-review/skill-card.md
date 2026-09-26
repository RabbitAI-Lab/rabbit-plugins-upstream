## Description:

Provides structured code review for diffs, pull requests, and individual files, covering correctness, security, performance, readability, and test coverage with severity-ranked findings and actionable recommendations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qq435912743](https://clawhub.ai/user/qq435912743)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to review code changes or files before merge or release, with findings grouped by severity and tied to concrete remediation advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The static checker is heuristic and may miss security, correctness, or architecture issues.

Mitigation: Use it as a pre-check and rely on semantic review and human judgment for high-impact changes.

Risk: The optional learning script writes a local learned_patterns.json file and can store user-provided notes.

Mitigation: Run it only against directories where local writes are acceptable, and avoid putting secrets, credentials, or private code excerpts in notes.

Risk: The source workflow and messages are written for a Chinese-language code-review process.

Mitigation: Use the skill only where Chinese-language review output is acceptable, or localize the workflow before deployment.

## Reference(s):


## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Structured Markdown review findings with severity labels, file and line references, actionable recommendations, and optional JSON output from the checklist script.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The static checklist can emit JSON for detected patterns such as hardcoded credential strings, bare except clauses, TODO markers, and long functions.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
