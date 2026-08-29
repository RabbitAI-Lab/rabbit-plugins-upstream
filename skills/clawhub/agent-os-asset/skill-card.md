## Description:

Agent OS Asset turns forgotten documents, archives, code projects, datasets, and media into privacy-aware, reviewable AI-ready assets that agents can retrieve and use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lee-agi](https://clawhub.ai/user/lee-agi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and knowledge workers use this skill to inventory historical files, generate reviewable agent-readable assets, make keep/archive/delete decisions, and build a final non-PII retrieval index after human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can receive broad access to folders selected by the user.

Mitigation: Keep scopes narrow, start with planning or dry-run modes, and review reports before enabling execution gates.

Risk: The skill can run adapter code from the folder being processed.

Mitigation: Inspect any <root>/tools/cleanup_convert.py before running it or enabling synchronization, especially for untrusted repositories.

Risk: Automatic synchronization can persist behavior through a macOS LaunchAgent.

Mitigation: Avoid auto-sync on untrusted repositories and disable synchronization when it is no longer needed.

Risk: Apply, delete, archive, synchronization, remote model use, and indexing stages can affect local files or expose selected content when enabled.

Mitigation: Use explicit execution flags only after reviewing dry-run reports, privacy classifications, and pending decision counts.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/lee-agi/skills/agent-os-asset)
- [Publisher profile](https://clawhub.ai/user/lee-agi)
- [README](artifact/README.md)
- [Security](artifact/SECURITY.md)
- [Agent readable document workflow](artifact/skills/agent-readable-doc/references/conversion-workflow.md)
- [Knowledge base review workflow](artifact/skills/kb-review/references/workflow.md)
- [Second brain privacy guidance](artifact/skills/second-brain/references/privacy.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands, JSON/JSONL manifests, generated .agent.md files, and local configuration artifacts.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Execution-changing stages are gated and may create local review reports, manifests, generated agent-readable files, and retrieval indexes only when explicitly enabled.]

## Skill Version(s):

0.1.1 (source: server release metadata, SKILL.md metadata, pyproject.toml, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
