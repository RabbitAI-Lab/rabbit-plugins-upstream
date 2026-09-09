## Description:

Experience-inheritance runtime for coding agents: recall validated fixes at task start, register hits when they are used, deposit newly learned fixes after repairing failures, and optionally run controlled closed-loop experiments to measure inheritance gains.

This skill is for research and development only.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent researchers use this skill to give a coding agent a controlled experience-inheritance loop for recalling validated fixes, registering useful recalls, and depositing new repair knowledge. It is also used to run closed-loop Pi and Evolver experiments that measure whether inherited fixes reduce repeated failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent inherited fixes can affect future agent sessions and may introduce misleading or unsafe guidance.

Mitigation: Inspect ~/.evomap/assets before reuse, keep the Pi bridge project-local, and review recalled fixes before applying them.

Risk: --auto-approve can weaken the intended manual review gate for newly distilled fixes.

Mitigation: Avoid --auto-approve for normal work and keep human approval for shared, sensitive, or production-adjacent environments.

Risk: --llm-refine can send session transcript content to the configured external endpoint.

Mitigation: Leave --llm-refine disabled for confidential repositories unless the endpoint is trusted and dedicated credentials are used.

Risk: --fresh clears the global Evolver asset store after creating a backup.

Mitigation: Use --fresh only for controlled experiments and confirm the backup location before relying on it for recovery.

Risk: Experiment outputs can contain task text, code, tool output, transcripts, and injected-fix text.

Mitigation: Store experiment directories securely and avoid sharing outputs that include private repository or customer context.

## Reference(s):

- [Pi EvoX Lab homepage](https://github.com/stwhwing/pi-evox-lab)
- [ClawHub skill page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Experiment report](docs/experiment-report.md)
- [Adapter design](docs/adapter-design.md)
- [pi-coding-agent package](https://www.npmjs.com/package/@earendil-works/pi-coding-agent)
- [@evomap/evolver package](https://www.npmjs.com/package/@evomap/evolver)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown instructions with command-line snippets and generated local experiment or gene-store artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write or read local Evolver assets, Pi session transcripts, experiment outputs, and optional injected-fix text when the user runs the documented commands.]

## Skill Version(s):

0.4.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
