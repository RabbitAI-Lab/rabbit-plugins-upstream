## Description:

Manages ARI Amazon ASIN watches and produces deterministic daily or weekly product snapshot change digests from saved snapshots and review counts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[funewa](https://clawhub.ai/user/funewa)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create, list, pause, resume, delete, and inspect Amazon ASIN snapshot watches in ARI, then receive deterministic watch digests for supported periods.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill stores an ARI API key locally and uses it for account-specific watch management.

Mitigation: Install only when ARI account access is intended, and remove the local ~/.ari/config.json key when monitoring is no longer needed.

Risk: Creating or changing watches can affect ARI account quotas or monitoring costs.

Mitigation: Review daily versus weekly quota and cost implications before creating or modifying watches.

Risk: Active watches may continue monitoring after the immediate task is complete.

Mitigation: Pause or delete server-side watches that are no longer required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/funewa/skills/asin-change)
- [Amazon ASIN change monitoring reference](references/reference.md)
- [Amazon ASIN change monitoring workflow](references/watch-workflow.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and structured ARI CLI responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires an ARI API key and user-requested watch actions; watch digest is documented as deterministic and zero credits.]

## Skill Version(s):

1.4.13 (source: server release evidence, artifact _meta.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
