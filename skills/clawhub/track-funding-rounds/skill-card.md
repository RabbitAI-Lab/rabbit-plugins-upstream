## Description:

Track recent funding rounds, amounts, and investors for companies using Cargo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cargo-ai](https://clawhub.ai/user/cargo-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External account executives and sales development professionals use this skill to identify recently funded target companies and review their funding rounds, amounts, and investors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Company domains are shared with Cargo and its funding connector.

Mitigation: Submit only company domains you are permitted to share with Cargo and its connector.

Risk: Large batches can consume credits across every submitted record.

Mitigation: Check the sample cost and hit rate first, then confirm the full record count and estimated credits before running a larger batch.

Risk: The npm dependencies and optional broader skill pack are outside this artifact review.

Mitigation: Review their versions and contents separately before use.

## Reference(s):

- [Cargo GTM skills project homepage](https://github.com/getcargohq/gtm-skills)
- [Funding watch recipe](https://github.com/getcargohq/cargo-skills/blob/main/cargo-gtm/recipes/funding-watch.md)
- [ClawHub release page](https://clawhub.ai/cargo-ai/skills/track-funding-rounds)

## Skill Output:

**Output Type(s):** [Text, Markdown]

**Output Format:** [Markdown table or concise text summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Funding details may be absent when no matching records are available.]

## Skill Version(s):

1.0.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
