## Description:

Uses saved Amazon product snapshots, deterministic diffs, and existing review counts to produce daily or weekly change summaries for a single ASIN; it requires an ARI API key and does not provide real-time price, sales, inventory, advertising, order, or return-rate data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External operators, sellers, and developers use this skill to create, list, pause, resume, delete, and inspect ARI-backed Amazon ASIN snapshot watches, then read deterministic watch digests for supported periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an ari_live_* API key saved under the local user profile or supplied through ARI_API_KEY.

Mitigation: Install only for intended ARI use, keep ~/.ari private and out of synced or shared folders, and rotate or revoke the key if exposure is suspected.

Risk: Watch management commands can pause, resume, or delete ARI watches for the account.

Mitigation: Run watch list first, review watch IDs carefully, and execute pause, resume, or delete only after the user explicitly requests the action.

Risk: The skill makes remote API calls to the ARI service for authorization, account checks, and watch operations.

Mitigation: Use the documented https://ari.funewa.com endpoint, stop on endpoint or redirect block errors, and do not bypass connection checks.

## Reference(s):

- [README](README.md)
- [Amazon ASIN Change Monitoring Reference](references/reference.md)
- [Watch Workflow](references/watch-workflow.md)
- [ARI Service](https://ari.funewa.com)
- [ClawHub Skill Page](https://clawhub.ai/funewa/skills/asin-change)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON CLI responses from ARI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces watch_digest summaries for supported 7d or 30d periods; deterministic digest reads use no paid LLM credits.]

## Skill Version(s):

1.4.11 (source: evidence.release.version, artifact/_meta.json, artifact/scripts/ari.py, artifact/CHANGELOG.md)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
