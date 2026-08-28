## Description:

AI记忆工程实战版 helps AI developers, cognitive-science learners, and agent architects turn learning-memory methodology into local memory-system reference code, evaluation, review scheduling, and memory-poisoning defenses.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent architects use this skill to design, evaluate, and harden local AI memory systems with layered storage, provenance metadata, review automation, and a runnable memory evaluation script.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included evaluation script reads local memory files and writes a JSON report when run manually.

Mitigation: Run it only against an intended memory directory and choose an output path that is safe to overwrite or create.

Risk: The security guidance notes that the script contains an encoded keyword list, which can make review less transparent.

Mitigation: Review the decoded keyword list before use, or replace it with plain documented configuration in deployments that require easier auditability.

Risk: The skill provides design-level memory-poisoning defenses, while artifact evidence states real red-team testing was not performed.

Mitigation: Use provenance checks, untrusted-memory gates, and periodic audits as documented, and perform separate adversarial testing before high-risk use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/ai-brain-learning-memory-pro)
- [调研出处与证据](artifact/references/调研出处与证据.md)
- [Memory evaluation battery](artifact/scripts/memory_eval_battery.py)
- [Security audit](artifact/SECURITY_AUDIT.md)

## Skill Output:

**Output Type(s):** [guidance, code, shell commands, configuration, markdown]

**Output Format:** [Markdown with Python and shell code blocks plus configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes a local zero-dependency Python evaluation script that can emit JSON results.]

## Skill Version(s):

1.0.0 (source: server release metadata, SKILL.md frontmatter, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
