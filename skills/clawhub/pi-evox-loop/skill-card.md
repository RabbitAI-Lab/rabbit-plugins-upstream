## Description:

Adds an experience-inheritance workflow for coding agents that recalls validated fixes, records their use, and deposits newly learned fixes, with optional controlled experiments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT-0

## Use Case:

Developers use it with coding agents to recall approved, task-relevant fixes and record useful repairs for future sessions. Researchers can run optional controlled experiments to assess experience inheritance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment identifies verified gaps in privacy checks, prompt safeguards, and experiment isolation.

Mitigation: Prefer manual local recall and deposit until the safeguard gaps are fixed. Review complete exported records, keep imported fixes quarantined, and inspect their metadata before approval.

Risk: Experiments can execute repository code, and the --root option alone does not isolate execution.

Mitigation: Run experiments in a disposable copy of the entire repository with a separate experience store. Back up existing hooks before using or changing them.

Risk: Optional model workflows send task, transcript, or fixture content to configured providers.

Mitigation: Review the content and destination before enabling these workflows; use a local or self-managed endpoint when appropriate.

## Reference(s):

- [Project repository](https://github.com/stwhwing/pi-evox-lab)
- [ClawHub release page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Security and license guidance](artifact/docs/security-and-license.md)
- [Project overview](artifact/docs/overview.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code]

**Output Format:** [Markdown guidance with shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Task-relevant recalled fixes and reviewable experience records]

## Skill Version(s):

0.36.0 (source: SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
