## Description:

Checks relaunch readiness for an existing Amazon ASIN using product details and collected review evidence, requiring an ARI API key and at least 10 reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and operators use this skill to check whether an existing ASIN is ready for a listing revision or relaunch. It guides an agent through ARI account checks, quote-before-charge workflows, product profile review, and evidence-based launch-readiness reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The installed CLI can perform broader ARI account operations than launch-readiness, including persistent monitoring, account data changes, exports, and paid actions.

Mitigation: Install and use it only when broad ARI account management is intended, and require explicit user confirmation before actions that change schedules, watches, competitors, review statuses, exports, or spend credits.

Risk: The ARI API key authorizes account access and is saved locally under ~/.ari/config.json.

Mitigation: Keep the key out of reports, command examples, and screenshots, and review or revoke the saved key when access is no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/launch-readiness)
- [ARI CLI 与 API 参考](references/reference.md)
- [Amazon 已有 ASIN 上线准备度检查 专属运营工作流](references/operation-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and ARI report links when returned by the service]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; paid ARI actions require an explicit quote and user confirmation before execution.]

## Skill Version(s):

1.4.3 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
