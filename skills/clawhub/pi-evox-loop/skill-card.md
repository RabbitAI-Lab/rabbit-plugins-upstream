## Description:

Experience-inheritance runtime for coding agents that recalls validated fixes from an Evolver gene store, records useful hits, deposits newly learned repair strategies, and can run controlled closed-loop experiments to measure inheritance gains.

This skill is for research and development only.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent researchers use this skill to give coding agents a controlled recall-and-deposit loop for previously validated repair strategies. It can also run Pi plus Evolver experiments that compare first-run failures with later runs that receive inherited fixes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent prompt-injection behavior may reuse unapproved or low-quality entries.

Mitigation: Use an isolated or single-user research environment, keep the bridge project-local, avoid --auto-approve for real work, and review the approval logic before sensitive use.

Risk: The experiment runner has command and path-handling flaws.

Mitigation: Review command construction and path handling before running on sensitive repositories or shared systems.

Risk: --llm-refine can send session transcripts to the configured external endpoint.

Mitigation: Leave --llm-refine disabled unless EVOLVER_REFINE_URL points to a trusted local or controlled endpoint for the transcript contents.

Risk: --fresh clears the global Evolver asset store after backup.

Mitigation: Run destructive experiments only after confirming the backup location and recovery plan.

Risk: Experiment outputs can contain task text, code, tool output, and injected fix content.

Mitigation: Store experiment directories with the same access controls used for source code and session transcripts.

## Reference(s):

- [Project homepage](https://github.com/stwhwing/pi-evox-lab)
- [Skill README](README.md)
- [Experiment report](docs/experiment-report.md)
- [Adapter design](docs/adapter-design.md)
- [Pi coding agent](https://www.npmjs.com/package/@earendil-works/pi-coding-agent)
- [Evolver](https://www.npmjs.com/package/@evomap/evolver)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, numbered fix lists, and experiment summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write local Evolver assets and experiment transcripts when the user runs the provided commands.]

## Skill Version(s):

0.3.3 (source: server release metadata; artifact frontmatter 0.3.2 and package.json 0.1.0 differ)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
