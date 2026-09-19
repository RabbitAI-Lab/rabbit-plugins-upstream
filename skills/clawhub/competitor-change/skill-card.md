## Description:

Summarizes observable changes in authorized Amazon competitor product snapshots on supported daily or weekly watch cycles using deterministic diffs and existing review counts; it does not provide real-time market data or sales, inventory, advertising, order, or return-rate conclusions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and Amazon marketplace operators use this skill to manage authorized competitor product watch records and read deterministic daily or weekly change digests for product snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires and stores an ARI API key for account access.

Mitigation: Install only for users who intend to connect an ARI account, and keep the local ARI configuration and ARI_API_KEY environment variable protected.

Risk: The skill contacts ari.funewa.com and depends on that external service for watch management and digest data.

Mitigation: Review the network dependency before deployment; the artifact documents official-domain HTTPS access and redirect blocking.

Risk: User-directed delete actions remove watch configuration.

Mitigation: Review watch delete requests carefully and execute them only when the user explicitly asks for deletion.

Risk: Watch digests can be mistaken for real-time market intelligence or complete sales, inventory, advertising, order, or return-rate data.

Mitigation: Treat outputs as deterministic summaries of observable product snapshot changes within supported periods, not as real-time or unavailable business metrics.

Risk: The artifact describes watch availability checks before use.

Mitigation: Confirm the local CLI exposes the watch subcommands before relying on the workflow; upgrade the skill if the commands are unavailable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/competitor-change)
- [ARI Service Endpoint](https://ari.funewa.com)
- [README](artifact/README.md)
- [Competitor Watch Workflow](artifact/references/watch-workflow.md)
- [Competitor Watch Reference](artifact/references/reference.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key. Watch digests are deterministic and documented as using zero analysis credits.]

## Skill Version(s):

1.4.13 (source: evidence.release.version, artifact/_meta.json, artifact/CHANGELOG.md, artifact/scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
