## Description:

Manages software delivery by designing, coding, testing, reviewing, auditing security, and preparing releases with defined roles and process gates.

This skill is ready for commercial/non-commercial use.

## Publisher:

[t3ratech](https://clawhub.ai/user/t3ratech)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this agent configuration bundle to move software work from a specification through design, implementation, testing, review, security checks, and release readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is intended to exercise normal software engineering authority over a codebase, including editing files and running shell commands.

Mitigation: Install it only where that authority is intended, review proposed changes before release, and keep testing, review, and security gates in the workflow.

Risk: A delivery workflow that reaches release preparation can propagate incorrect code, tests, or security conclusions if its outputs are accepted without review.

Mitigation: Run the bundled evaluation set before use and require human review of implementation, test, security, and release outputs before publishing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/t3ratech/skills/software-delivery-team)
- [Publisher profile](https://clawhub.ai/user/t3ratech)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline code, commands, review notes, and release guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include code edits, tests, review findings, security guidance, changelog notes, and release-readiness recommendations.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
