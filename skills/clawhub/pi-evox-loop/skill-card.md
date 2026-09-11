## Description:

Pi EvoX Loop gives coding agents an experience-inheritance runtime that recalls approved repair strategies, records used fixes, deposits newly learned fixes, and can run controlled R1 -> distill -> inject -> R2 experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding agents use this skill to carry validated repair experience across sessions, recall relevant fixes at the start of non-trivial tasks, and capture non-obvious fixes after debugging. Teams can also run controlled experiments to measure whether inherited fixes reduce repeated errors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A persistent experience store can influence future agent prompts with weak relevance controls.

Mitigation: Keep manual review enabled, periodically review approved entries, and prefer project-local extensions over global extensions.

Risk: Combining automatic approval with LLM refinement can let unreviewed rewritten fixes enter future sessions.

Mitigation: Avoid --auto-approve with --llm-refine outside isolated experiments, or require explicit human review before approval.

Risk: Generated transcripts and experiment directories can contain task text, code, tool output, and other sensitive context.

Mitigation: Treat generated experiment directories as sensitive, use restricted API keys, and avoid enabling transcript export to external endpoints unless approved.

Risk: --fresh can clear the shared Evolver asset store after making a backup.

Mitigation: Run destructive experiment modes only in isolated workspaces and confirm backups before relying on stored repair history.

## Reference(s):

- [Pi EvoX Lab homepage](https://github.com/stwhwing/pi-evox-lab)
- [Security and license details](docs/security-and-license.md)
- [Experiment report](docs/experiment-report.md)
- [Adapter design](docs/adapter-design.md)
- [Other agent integration guide](docs/other-agents.md)
- [Provider configuration examples](docs/providers.md)
- [pi-coding-agent package](https://www.npmjs.com/package/@earendil-works/pi-coding-agent)
- [Evolver package](https://www.npmjs.com/package/@evomap/evolver)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline command examples and CLI text output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce numbered recalled fixes, hit-registration logs, experiment summaries, and local configuration snippets.]

## Skill Version(s):

0.10.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
