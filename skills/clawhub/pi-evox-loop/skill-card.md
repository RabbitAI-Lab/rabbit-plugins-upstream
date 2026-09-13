## Description:

Pi EvoX Loop gives coding agents an experience-inheritance runtime for recalling validated fixes, recording used fixes, depositing new repair strategies, and optionally running controlled closed-loop experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding-agent operators use this skill to make repair knowledge reusable across non-trivial coding tasks. It supports task-start recall, post-fix knowledge capture, hit registration, and optional controlled experiments for measuring whether inherited fixes reduce repeated failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent stored repair strategies can influence future agent prompts across tasks or projects.

Mitigation: Use an isolated EVO_STORE_DIR or project-local Pi extension, manually review stored strategies, and periodically inspect the experience store before reuse.

Risk: Approval and revocation controls are reported as broken in the authoritative security evidence.

Mitigation: Do not rely on quarantine or revocation until approval-state logic is fixed; manually review strategies before they are injected.

Risk: The optional --llm-refine path can send session transcript content to an external endpoint.

Mitigation: Keep --llm-refine disabled unless the endpoint is explicitly trusted, or use a local or controlled endpoint with reviewed data handling.

Risk: --auto-approve can allow unreviewed strategies to affect later runs.

Mitigation: Avoid --auto-approve outside controlled experiments and retain the default human review gate for normal use.

Risk: --fresh clears the experience store after backup and can disrupt existing shared memory state.

Mitigation: Run destructive experiment modes only in isolated stores and confirm backups before clearing existing assets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project homepage](https://github.com/stwhwing/pi-evox-lab)
- [Security and license notes](docs/security-and-license.md)
- [Adapter design](docs/adapter-design.md)
- [Experiment report](docs/experiment-report.md)
- [Other agent integration](docs/other-agents.md)
- [Provider configuration](docs/providers.md)
- [Pi coding agent](https://github.com/earendil-works/pi)
- [EvoMap Evolver](https://github.com/EvoMap/evolver)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and plain text with inline shell commands, configuration snippets, and code-oriented guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read from and write to a persistent experience store; optional experiment mode can produce session transcripts, run logs, generated trap fixtures, and token/error summaries.]

## Skill Version(s):

0.12.0 (source: package.json and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
