## Description:

Give your coding agent an experience-inheritance runtime that recalls validated fixes at task start, registers hits when fixes are used, and deposits newly learned fixes after non-obvious failures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[stwhwing](https://clawhub.ai/user/stwhwing)

### License/Terms of Use:

MIT

## Use Case:

Developers and coding-agent operators use this skill to preserve hard-won repair knowledge, recall relevant fixes on later tasks, and run controlled experiments that measure whether inherited fixes reduce repeated failures.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A shared persistent experience store can influence later agent prompts across tasks or projects.

Mitigation: Use a project-scoped EVO_STORE_DIR where possible, keep reviewed entries narrow and actionable, and periodically inspect stored repairs.

Risk: Unreviewed refinement or auto-approval can allow low-quality or misleading learned fixes into future sessions.

Mitigation: Keep manual review enabled for untrusted projects and avoid --auto-approve and --allow-unreviewed-refine unless the deployment context explicitly accepts that risk.

Risk: LLM refinement can send session excerpts to an external endpoint when explicitly enabled.

Mitigation: Use a trusted HTTPS refinement endpoint, a separate limited API key, and disable refinement when session content should remain local.

Risk: Global bridge installation can introduce inherited-fix behavior outside the intended project.

Mitigation: Install the Pi bridge at project scope unless cross-project behavior is intentional and documented.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/stwhwing/skills/pi-evox-loop)
- [Project Homepage](https://github.com/stwhwing/pi-evox-lab)
- [Experiment Report](docs/experiment-report.md)
- [Adapter Design](docs/adapter-design.md)
- [Provider Configuration](docs/providers.md)
- [Security and License](docs/security-and-license.md)
- [Other Agent Hosts](docs/other-agents.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown instructions with inline shell commands and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May persist reviewed repair entries and emit recall lists, hit registrations, experiment summaries, and setup guidance.]

## Skill Version(s):

0.14.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
