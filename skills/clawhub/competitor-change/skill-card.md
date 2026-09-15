## Description:

Summarizes observable Amazon competitor product snapshot changes on supported ARI watch schedules using deterministic diffs and existing review counts, and requires an ARI API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External marketplace operators and agents use this skill to create, manage, and summarize ARI competitor product watches for authorized Amazon products. It supports deterministic daily or weekly snapshot monitoring, not real-time market data, sales, inventory, advertising, order, or true return-rate conclusions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an ARI API key and can access ARI account data.

Mitigation: Install only when ARI competitor watch access is intended, keep ~/.ari private, avoid syncing that directory to shared or cloud folders, and revoke or regenerate the key if local account compromise is suspected.

Risk: Create and delete actions change ARI-side monitoring state.

Mitigation: Review the intended watch action before execution and run management commands only after the user clearly requests the change.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/competitor-change)
- [ARI service](https://ari.funewa.com)
- [Competitor change monitoring reference](references/reference.md)
- [Competitor watch workflow](references/watch-workflow.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with ARI CLI commands and JSON command responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Digest output is documented as deterministic and zero-credit; watch management commands can change ARI-side monitoring state.]

## Skill Version(s):

1.4.11 (source: server release metadata, _meta.json, CHANGELOG, scripts/ari.py)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
