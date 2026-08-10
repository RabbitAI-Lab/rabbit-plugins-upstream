## Description:

LYGO CLI Bridge provides a local CLI entrypoint for LYGO health, map, analysis, mint, radar, next, and version workflows while using in-process companion imports and avoiding subprocesses or auto-publish actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[deepseekoracle](https://clawhub.ai/user/deepseekoracle)

### License/Terms of Use:

MIT No Attribution (MIT-0)

## Use Case:

Developers and operators use this skill to run local LYGO protocol-stack workflows from one CLI, including public health checks, ecosystem mapping, text analysis, mint guidance, radar feed generation, and roadmap/status output.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Companion skills are imported from local directories and can affect analysis, mint, or radar behavior.

Mitigation: Install only trusted companion skills and keep LYGO_STACK_ROOT pointed at directories you control.

Risk: Text analysis can process private logs or mail if a user supplies them.

Mitigation: Do not pass private content to analyze unless the user has consent to process it.

Risk: Radar JSON or mint outputs can write files when explicitly requested.

Mitigation: Review output paths before using --out-json or mint flows with --i-consent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/deepseekoracle/skills/lygo-cli-bridge)
- [ClawHub publisher profile](https://clawhub.ai/user/deepseekoracle)
- [OpenClaw homepage](https://github.com/DeepSeekOracle/lygo-protocol-stack/tree/main/docs/skills/lygo-cli-bridge)
- [Security reference](references/SECURITY.md)
- [Quickstart](examples/quickstart.md)
- [Haven Star Chart](https://deepseekoracle.github.io/lygo-protocol-stack/HavenStarChart.html)
- [Deception Radar public proof](https://deepseekoracle.github.io/lygo-protocol-stack/deception-radar/)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance, Configuration]

**Output Format:** [Markdown instructions and JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local-first CLI responses; optional file writes require explicit --i-consent.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, claw.json, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
