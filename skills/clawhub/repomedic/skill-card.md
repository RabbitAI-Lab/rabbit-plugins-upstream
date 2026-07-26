## Description: <br>
Safely triage and remediate GitHub dependency hygiene issues with explicit guardrails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mrummler17](https://clawhub.ai/user/mrummler17) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and maintainers use RepoMedic to triage failing Dependabot updates, dependency security alerts, lockfile drift, and CI or preview-build dependency failures while keeping remediation scoped and reviewable. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Dependency remediation can change repository files, package versions, or lockfiles in ways that affect builds or runtime behavior. <br>
Mitigation: Keep work on a non-default branch, show planned files and version changes before execution, and require explicit approval for major upgrades or medium/high-risk dependency changes. <br>
Risk: Package-manager and validation commands can alter local workspace state or produce incomplete confidence if checks are skipped. <br>
Mitigation: Limit work to the target repository, run available install, build, test, lint, and audit checks, and report validation results and remaining risks. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance, Code, Shell commands, Configuration] <br>
**Output Format:** [Structured Markdown sections with optional inline code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes issue summary, recommended action, risk level, changed files and versions, validation results, plain-English summary, and next step.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
