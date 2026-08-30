## Description:

Protect agent memory: snapshot before compaction, scan memory/snapshot files for prompt-injection, secrets, and contradictions, audit what changed. Use when hardening agent memory or auditing for indirect prompt injection. Don't use for general code SAST or SQL scanning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vnbochkarev-netizen](https://clawhub.ai/user/vnbochkarev-netizen)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to snapshot text-based agent memory before compaction, scan memory or snapshots for suspicious injected instructions, contradictions, anomalies, and secrets exposure, and audit changes between snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-selected memory files and directories, which may contain sensitive information.

Mitigation: Point it only at intended memory stores and avoid broad home directories or unrelated sensitive locations.

Risk: The scanner is heuristic and may miss carefully disguised prompt injection or contradiction patterns.

Mitigation: Treat clean scan results as review support, not proof of safety, and manually review high-risk imported memory.

Risk: Snapshots protect only the files captured at the time they are run.

Mitigation: Run snapshots before compaction and before major memory changes so important context is included.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/vnbochkarev-netizen/skills/memory-shield)
- [Publisher profile](https://clawhub.ai/user/vnbochkarev-netizen)
- [Referenced GitHub repository](https://github.com/vnbochkarev-netizen/memory-shield)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown reports and console text with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local snapshot, scan report, and audit output files; scanner findings are quarantined in reports rather than deleted.]

## Skill Version(s):

0.1.5 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
