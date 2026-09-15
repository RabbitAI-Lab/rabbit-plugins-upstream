## Description:

Long-term verification agents for the PASM cognitive engine that run repeatable checks for memory retention, salience-aware eviction, emotion drift, behavioral entropy collapse, persona saturation, forgetting curve behavior, 6000-step soak degradation, and cross-repo parity.

This skill is ready for commercial/non-commercial use.

## Publisher:

[arronjack](https://clawhub.ai/user/arronjack)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to verify whether PASM cognitive-engine behavior remains healthy after long runs. It supports repeatable local checks, JSON archiving, CI integration, baseline comparison, and troubleshooting for PASM agent packages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow installs and runs an unpinned external Python package.

Mitigation: Use a virtual environment or disposable developer workspace and review or pin pasm-agents and pasm-skills versions before use.

Risk: Running verification commands in a developer environment could expose local secrets to package code or subprocesses.

Mitigation: Avoid running the skill with production secrets exposed and prefer isolated workspaces for verification runs.

Risk: Key setup, warning, and troubleshooting sections are written primarily in Chinese.

Mitigation: Non-Chinese readers should confirm the setup and warning sections before relying on the results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/arronjack/skills/pasm-longterm-verify)
- [pasm-agents repository](https://github.com/arronJack/pasm-agents)
- [pasm-skills repository](https://github.com/arronJack/pasm-skills)
- [pasm-skills tutorial](https://github.com/arronJack/pasm-skills/blob/master/docs/TUTORIAL.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON-report options]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires python3 and git; checks can emit OK, WARN, FAIL, and SKIP results and optionally archive JSON findings.]

## Skill Version(s):

0.4.9 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
