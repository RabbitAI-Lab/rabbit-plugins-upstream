## Description:

Pi EvoX Loop gives coding agents an experience-inheritance runtime for recalling validated Evolver fixes, registering used fixes, depositing new fixes after non-obvious failures, and optionally running controlled closed-loop experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and engineers use this skill to help coding agents reuse reviewed repair strategies across tasks and to measure closed-loop experience inheritance on controlled failure traps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Unapproved or low-quality memory may be injected into future prompts.

Mitigation: Keep manual review enabled and avoid --auto-approve outside controlled experiments.

Risk: --llm-refine can send transcript content to a configured external endpoint.

Mitigation: Use only local or trusted refinement endpoints, and leave refinement variables unset unless transcript data may leave the machine.

Risk: Experiment mode can clear the global Evolver store and leave artifacts containing task text, code, and tool output.

Mitigation: Run experiments in a throwaway checkout with a dedicated Evolver store and protect or remove generated run artifacts.

Risk: Runner shell and cleanup behavior may execute commands or delete local data if misused or affected by bugs.

Mitigation: Review runner code before execution and run high-risk experiments in a disposable workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage](https://github.com/stwhwing/pi-evox-lab)
- [README](README.md)
- [Experiment report](docs/experiment-report.md)
- [Adapter design](docs/adapter-design.md)
- [pi-coding-agent](https://www.npmjs.com/package/@earendil-works/pi-coding-agent)
- [Evolver](https://github.com/EvoMap/evolver)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and code/configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose commands that read or update a local Evolver gene store; optional experiment mode can create local run artifacts.]

## Skill Version(s):

0.5.0 (source: SKILL.md frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
