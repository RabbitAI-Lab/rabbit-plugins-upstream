## Description:

Merges ephemeral report and analysis artifacts into permanent documentation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technical writers use this skill to find temporary LLM-generated report markdown, plan which useful content belongs in permanent documentation, and execute approved documentation merges.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Approved consolidation can delete source report files after merging, and deleted sources are not automatically restorable.

Mitigation: Review the proposed destination files and deletion list before approval; keep a backup or commit or stash source reports when they must be retained.

Risk: Merged report content may add outdated, low-value, or misplaced analysis to permanent documentation.

Mitigation: Review the consolidation plan for selected chunks, destinations, and skipped content before execution, then review generated or updated docs before committing.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-sanctum-doc-consolidation)
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/sanctum)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown plans, documentation edits, shell command snippets, and execution summaries.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create or update markdown documentation and delete approved source artifacts after successful consolidation.]

## Skill Version(s):

1.9.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
