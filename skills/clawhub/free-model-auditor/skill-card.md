## Description:

Audits a WorkBuddy models.json registry for free OpenAI-compatible chat models, tests candidates across supported providers, and applies targeted additions or removals with reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[igenomed](https://clawhub.ai/user/igenomed)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and WorkBuddy users use this skill to keep a custom free-model registry current by checking configured providers, validating candidate chat models, and generating an audit report with safe registry updates.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses API keys stored in models.json to contact third-party model providers.

Mitigation: Run it only in trusted workspaces where live provider calls are acceptable, and rotate provider keys if exposure is suspected.

Risk: The skill can modify the user's model registry without a separate confirmation step.

Mitigation: Review the dry-run diff before applying changes, keep the generated backup, and rely on targeted add/remove operations with invariant checks.

Risk: Some providers do not expose reliable free-tier fields, so live success alone may not prove a model is free.

Mitigation: Use the provider-specific free-model criteria and review uncertain entries in the provider console before treating them as zero-cost.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/igenomed/skills/free-model-auditor)
- [Platform audit knowledge base](references/platforms.md)
- [Live provider test harness](references/test_harness.py)
- [Safe registry diff applier](references/apply_diff.py)
- [Portable path resolver](references/resolve_paths.py)
- [Audit report template](templates/audit_report.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON diffs, shell command guidance, and targeted models.json configuration updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May create an audit report, daily log, models.json backup, and targeted registry changes while using stored provider API keys for live checks.]

## Skill Version(s):

1.6.0 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
