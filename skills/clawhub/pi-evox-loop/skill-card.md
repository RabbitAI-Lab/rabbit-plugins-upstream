## Description:

Experience-inheritance runtime for coding agents: recall validated fixes at task start, register hits when used, deposit fixes after repairing failures, and optionally run controlled closed-loop experiments to measure inheritance gains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding-agent operators use this skill to add persistent, reviewed repair recall to coding agents and to measure inheritance gains through optional controlled experiments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent coding-agent memory can read local session histories and influence later prompts.

Mitigation: Install only in environments where that behavior is intended, keep manual review enabled, and scan stored fixes before deployment.

Risk: LLM refinement can send session transcripts to an external endpoint when explicitly enabled.

Mitigation: Leave LLM refinement disabled unless an approved endpoint and data-handling path are in place.

Risk: One experiment/injection path can keep using previously approved memories after quarantine.

Mitigation: Avoid relying on quarantine revocation in the pi_evolve CLI path until the approval-state bug is fixed, and isolate test stores with EVO_STORE_DIR.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage](https://github.com/stwhwing/pi-evox-lab)
- [Security and license notes](docs/security-and-license.md)
- [Provider configuration](docs/providers.md)
- [Experiment report](docs/experiment-report.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update a persistent local experience store when commands are executed by the agent.]

## Skill Version(s):

0.14.3 (source: SKILL.md frontmatter, package.json, evidence.release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
