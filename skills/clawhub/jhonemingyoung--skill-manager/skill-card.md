## Description:

Plugin & Skill management assistant: scans and analyzes all installed Plugins/Skills, evaluates functionality, features, dependencies, and potential risks, and recommends matching Skills based on current task complexity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[jhonemingyoung](https://clawhub.ai/user/jhonemingyoung)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to inventory installed Plugins and Skills, assess task complexity, compare execution options, and produce recommendation reports before choosing an execution path.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says the skill can scan installed skills broadly, which may expose local skill inventory details in reports.

Mitigation: Run scans only against intended skill directories and review generated reports before sharing them outside the execution environment.

Risk: The security evidence says the skill recommends unpinned npx execution for external skill discovery.

Mitigation: Verify the package, version, publisher, and execution environment before running any suggested npx command.

Risk: The security evidence says the skill is a heuristic inventory and recommendation helper, not a security-grade audit tool.

Mitigation: Treat risk labels as triage signals and perform separate source review or security scanning before installation or deployment decisions.

## Reference(s):

- [Risk Assessment Reference Guide](references/risk_assessment.md)
- [ClawHub skill page](https://clawhub.ai/jhonemingyoung/skills/skill-manager)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown reports, JSON inventory, and plain-text tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports compare token cost, execution time, match quality, and risk; recommended actions require user selection before execution.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
