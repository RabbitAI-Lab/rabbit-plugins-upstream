## Description:

Long-term verification agents for the PASM cognitive engine run repeatable checks for memory retention, salience-aware eviction, emotion drift, behavioral entropy collapse, persona saturation, forgetting curve behavior, 6000-step soak degradation, and cross-repo parity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arronjack](https://clawhub.ai/user/arronjack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and maintainers use this skill to install and run PASM verification agents that check whether PASM repositories and cognitive-engine behaviors remain healthy across long-running scenarios and regression baselines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the installation and verifier commands executes third-party Python code against local PASM repositories.

Mitigation: Review the referenced pasm-agents, pasm-skills, and pasm-framework packages before installation and run them in an appropriate development environment.

Risk: Implicit or incorrect PASM repository paths could cause the verifier to inspect unintended projects.

Mitigation: Set explicit PASM_* paths so each verifier run targets only the intended PASM repositories.

Risk: Using regression --update changes the comparison baseline used for future checks.

Mitigation: Update the regression baseline only after confirming that the current state is the desired baseline.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arronjack/skills/pasm-longterm-verify)
- [PASM agents repository](https://github.com/arronJack/pasm-agents)
- [PASM skills repository](https://github.com/arronJack/pasm-skills)
- [PASM skills tutorial](https://github.com/arronJack/pasm-skills/blob/master/docs/TUTORIAL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and optional JSON report output from the PASM verifier commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Verifier runs can emit OK, WARN, FAIL, or SKIP findings and baseline-diffable JSON reports.]

## Skill Version(s):

0.4.11 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
