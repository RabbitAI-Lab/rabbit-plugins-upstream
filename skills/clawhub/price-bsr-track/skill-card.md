## Description:

Tracks deterministic changes in saved Amazon product snapshots, summarizing display price and primary BSR fields with sample timestamps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External Amazon operators and developers use this skill to create, manage, and read price/BSR snapshot watches for specific ASINs. It is for field-level tracking and deterministic watch digests, not real-time pricing, sales prediction, inventory management, advertising operations, order handling, or automatic repricing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an ARI API key and sends Amazon ASIN/watch data to the ARI service.

Mitigation: Install only if the user trusts ARI with that account credential and watch data; use setup or configure knowingly and keep the API key in the user's local ARI configuration.

Risk: Creating or resuming daily or weekly watches can have quota or scan-cost implications.

Mitigation: Review the account's daily or weekly quota and scan-cost impact before creating, resuming, or modifying watches.

Risk: Watch digests can be misread as real-time price, live BSR, sales, inventory, advertising, order, or repricing signals.

Mitigation: Use the output only as a deterministic summary of saved snapshot fields and switch to an explicitly confirmed separate workflow for AI weekly reporting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/price-bsr-track)
- [funewa publisher profile](https://clawhub.ai/user/funewa)
- [Amazon price and BSR tracking reference](artifact/references/reference.md)
- [Amazon price and BSR watch workflow](artifact/references/watch-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The watch digest is deterministic and limited to saved snapshot fields; setup and configure operations may store an ARI API key in the user's local ARI configuration.]

## Skill Version(s):

1.4.11 (source: server evidence, _meta.json, CHANGELOG, and scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
