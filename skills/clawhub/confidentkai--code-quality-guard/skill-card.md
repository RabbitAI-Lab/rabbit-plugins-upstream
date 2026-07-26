## Description: <br>
Pair-style code quality reviewer for code, PR, architecture, test-quality, technical-debt, and release-safety reviews using structured risk findings and a review-index Health Score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[confidentkai](https://clawhub.ai/user/confidentkai) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use this skill to perform structured code-quality reviews before merge, refactoring, architecture changes, test updates, or release gates. It helps agents produce prioritized findings with diagnosis, consequence, remedy, and a per-run Health Score. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Review suggestions can be incomplete or misleading if the agent misreads the code or applies the risk matrix too mechanically. <br>
Mitigation: Treat reports as advisory, check each finding against the cited source code, and review proposed remedies before applying changes. <br>
Risk: Optional repository extras can make review behavior automatic or block certain dangerous shell commands when wired into an agent. <br>
Mitigation: Review AGENTS-template.md and hooks.json before enabling them, and install those extras only in repositories where that behavior is desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/confidentkai/skills/code-quality-guard) <br>
- [README](README.md) <br>
- [Skill entrypoint](SKILL.md) <br>
- [Shared review framework](references/common.md) <br>
- [Production decay risks](references/decay-risks.md) <br>
- [Test decay risks](references/test-decay-risks.md) <br>
- [Editorial extensions](references/editorial-extensions.md) <br>
- [PR review guide](references/pr-review-guide.md) <br>
- [Source coverage](references/source-coverage.md) <br>
- [Examples](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Code] <br>
**Output Format:** [Markdown review report with structured findings; optional code edits only when the user explicitly asks for fixes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Findings follow Symptom, Source, Consequence, and Remedy; the Health Score is a per-run deduction index, not an objective codebase grade.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
