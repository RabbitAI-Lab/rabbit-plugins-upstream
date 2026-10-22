## Description:

Memory Orchestrator provides long-term memory management and retrieval across devices, with semantic search, multimodal input processing, emotion tagging, knowledge graph generation, and self-optimization workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[822376583-hub](https://clawhub.ai/user/822376583-hub)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add searchable long-term memory, multimodal memory ingestion, knowledge graph reporting, emotion tagging, proactive recommendations, and cross-device memory synchronization to a ClawHub agent environment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installer and workflows can enable persistent background behavior through systemd, cron, file-watch triggers, and session hooks.

Mitigation: Review and run in an isolated environment first; remove or gate sudo systemd actions, cron entries, and hooks until the operator has approved them.

Risk: Memory files, recordings, images, and derived state may be committed, pushed, or synchronized across devices.

Mitigation: Validate the Git remote, Syncthing device list, and git-crypt setup before syncing; test with non-sensitive data and restrict synchronized paths.

Risk: Proactive recommendation triggers may inject stored memory into future agent contexts without clear user consent.

Mitigation: Disable proactive triggers by default or require explicit consent and logging before recommendations are surfaced.

Risk: Dependencies are broad and not fully pinned, including a dependency installed from a Git URL.

Mitigation: Pin dependency versions, install in a virtual environment, and review package sources before use with private or work data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/822376583-hub/skills/memory-orchestrator)
- [Artifact README](artifact/README.md)
- [Artifact SKILL.md](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands, Python scripts, YAML workflows, JSON and HTML reports, and local index files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create local indexes, logs, reports, scheduled sync jobs, and memory state files when installed or run.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
