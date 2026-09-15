## Description:

Review Keywords uses ARI to analyze collected Amazon review samples, extract frequent and co-occurring customer wording, separate positive and negative themes, and produce review-backed keyword, VOC, trend, monitoring, and export outputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon sellers and ecommerce operators use this skill with an ARI API key to inspect collected reviews, find recurring buyer language and pain points, generate review-backed keyword or VOC guidance, monitor changes, and export review or report artifacts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use broad ARI review-management capabilities, not only keyword extraction.

Mitigation: Install it only for agents and users that should have access to the connected ARI account, and use a dedicated ARI API key that can be revoked if needed.

Risk: Some paid analysis actions can execute under the account's auto-confirm policy.

Mitigation: Review the account confirmation setting before paid analysis and use quote-only requests when the user wants pricing without execution.

Risk: Exports can overwrite files inside the allowed export directory.

Mitigation: Keep ARI_EXPORT_DIR unset or pointed at a dedicated export folder, and review explicit export paths before running export commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/review-keywords)
- [README](artifact/README.md)
- [Usage guide](artifact/%E4%BD%BF%E7%94%A8%E8%AF%B4%E6%98%8E.md)
- [ARI CLI and API reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries and reports, JSON CLI responses, CSV exports, HTML or Markdown report exports, and shell commands for setup or troubleshooting.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key; outputs depend on available collected review samples, site coverage, account entitlements, and paid action confirmation state.]

## Skill Version(s):

1.4.11 (source: server release evidence, SKILL.md frontmatter, _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
