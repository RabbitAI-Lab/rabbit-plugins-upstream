## Description:

Automates setup, configuration, execution, monitoring, and troubleshooting of AutoResearchClaw, a 23-stage autonomous research pipeline for generating conference-style research papers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[othmanadi](https://clawhub.ai/user/othmanadi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to configure and run AutoResearchClaw, monitor long pipeline runs, resume or diagnose failures, and collect generated paper artifacts. It is intended for agent-assisted autonomous research workflows where users provide the research topic, credentials, execution mode, and approvals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can run a long autonomous research pipeline while skipping human approval gates and using external services or code execution modes.

Mitigation: Review before installing, keep simulated mode and manual approval gates enabled for first runs, and avoid --auto-approve when using sandbox or ssh_remote modes.

Risk: Research topics, prompts, and generated experiment code may be sent to external providers or executed in local, Docker, or SSH environments.

Mitigation: Do not provide confidential research topics or regulated data to external providers, and manually review Docker-group changes, sudo installs, SSH keys, and generated experiment code.

## Reference(s):

- [Server-Resolved Source Import](https://github.com/OthmanAdi/researchclaw-skill/tree/main/skills/researchclaw)
- [ClawHub Skill Page](https://clawhub.ai/othmanadi/skills/researchclaw-2)
- [AutoResearchClaw Upstream Repository](https://github.com/aiming-lab/AutoResearchClaw)
- [AutoResearchClaw Configuration Reference](artifact/references/config-reference.md)
- [AutoResearchClaw Pipeline Stages Reference](artifact/references/pipeline-stages.md)
- [AutoResearchClaw Troubleshooting Guide](artifact/references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, YAML configuration, and status or diagnostic text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate config.yaml and local run logs or research artifacts when the user approves execution.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
