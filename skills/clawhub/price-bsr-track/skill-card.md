## Description:

Summarizes deterministic changes in saved Amazon product snapshots for display price and key Best Sellers Rank fields, with sampling times, through the ARI watch workflow.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce operators and their agents use this skill to list, create, pause, resume, delete, and inspect ARI product watches for saved Amazon snapshot price and BSR changes. It is for snapshot field tracking and deterministic watch digests, not real-time pricing, sales prediction, inventory management, advertising, orders, or automatic repricing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires an ari_live_* API key for the ARI service and can manage product watches for the user's account.

Mitigation: Confirm the user trusts the ARI service before setup, store the key only in the user configuration or ARI_API_KEY environment variable, and revoke the key from the ARI account if exposure is suspected.

Risk: Watch create, pause, resume, and delete commands change ongoing daily or weekly server-side monitoring state.

Mitigation: Run watch list before state changes, explain schedule quotas and scan costs before creating or changing watches, and execute only actions the user explicitly requested.

Risk: The skill does not provide real-time price or BSR monitoring, true sales or ranking prediction, inventory data, advertising data, order actions, or automatic repricing.

Mitigation: Present results as saved snapshot tracking only, preserve the documented workflow boundary, and direct requests for weekly AI reports or unsupported operations to the appropriate separate workflow.

Risk: The skill makes authenticated network calls to the ARI service.

Mitigation: Use only the documented https://ari.funewa.com origin, stop on endpoint or redirect blocking errors, and do not bypass the connection safety checks.

## Reference(s):

- [Amazon Price and BSR Watch Reference](artifact/references/reference.md)
- [Amazon Price and BSR Watch Workflow](artifact/references/watch-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON, guidance]

**Output Format:** [Markdown guidance with bash commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ari_live_* API key; watch digest output is deterministic and documented as zero-credit.]

## Skill Version(s):

1.4.13 (source: evidence.release.version, _meta.json, CHANGELOG, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
