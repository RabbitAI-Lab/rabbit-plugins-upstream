## Description:

Audit installed AI skills and recommend keep, archive, or uninstall actions to keep a user's skill set lean and focused.

This skill is ready for commercial/non-commercial use.

## Publisher:

[helloyxs](https://clawhub.ai/user/helloyxs)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users use this skill to scan installed skills across supported agent platforms, score their value, and produce bilingual keep, archive, or uninstall recommendations. It is useful for reducing duplicate, stale, or low-value skills while preserving cleanup decisions for user review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill enumerates local skill folders and reports installed-skill metadata.

Mitigation: Install only if local skill inventory disclosure is acceptable, and limit scans to the intended agent, workspace, or custom directory.

Risk: Cleanup recommendations may affect installed skills if the user proceeds with archive or uninstall actions.

Mitigation: Review every keep, archive, and uninstall recommendation before acting; confirm cleanup actions one by one.

Risk: Broad scan options such as --all, --workspace, custom directories, and archive scanning can expand the set of local files inspected.

Mitigation: Use the narrowest scan scope that answers the audit question and verify custom paths before running.

## Reference(s):

- [Evaluation Framework](references/evaluation_framework.md)
- [Skill page](https://clawhub.ai/helloyxs/skills/skill-subtraction)

## Skill Output:

**Output Type(s):** [analysis, markdown, shell commands, guidance]

**Output Format:** [Markdown report with optional shell commands and structured recommendation tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports English and Chinese reports; scan output may include installed-skill metadata, archived-skill inventory, issues, and cleanup recommendations.]

## Skill Version(s):

1.1.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
