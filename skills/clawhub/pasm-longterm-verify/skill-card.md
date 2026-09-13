## Description:

Long-term verification agents for the PASM cognitive engine run repeatable checks for memory retention, salience-aware eviction, emotion drift, behavioral entropy collapse, persona saturation, forgetting curves, 6000-step soak degradation, and cross-repo parity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arronjack](https://clawhub.ai/user/arronjack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to run long-duration structural and behavioral verification against PASM repositories, then archive or compare OK/WARN/FAIL findings as JSON-capable regression evidence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks users to install and run third-party Python packages against local PASM repositories.

Mitigation: Use a virtual environment or container, pin package versions or commit SHAs, and run with read-only repository access where possible.

Risk: Repository verification may touch local project paths and environment configuration.

Mitigation: Run only against intended PASM repositories and avoid exposing credentials or unrelated environment variables.

Risk: WARN and SKIP outcomes can be misread as successful verification.

Mitigation: Review non-OK details before accepting a run, especially safety-critical companion or long-duration behavior checks.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arronjack/skills/pasm-longterm-verify)
- [PASM agents repository](https://github.com/arronJack/pasm-agents)
- [PASM skills base repository](https://github.com/arronJack/pasm-skills)
- [PASM skills tutorial](https://github.com/arronJack/pasm-skills/blob/master/docs/TUTORIAL.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON report options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verification runs produce OK/WARN/FAIL/SKIP statuses and can write archiveable, baseline-diffable JSON reports.]

## Skill Version(s):

0.4.2 (source: server release metadata; artifact frontmatter reports 0.4.1)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
