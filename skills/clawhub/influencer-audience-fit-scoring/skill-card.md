## Description:

Pre-campaign audience quality and follower authenticity analysis across TikTok, Instagram, and YouTube, including geography, language, age, gender, interests, and creator comparison.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chengyu-xixihaha](https://clawhub.ai/user/chengyu-xixihaha)

### License/Terms of Use:

MIT-0

## Use Case:

External marketers, creator partnership teams, and agents use this skill before campaigns to evaluate whether a creator's audience matches an ICP and whether follower authenticity supports a go, test, or no-go decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creator research requests may be routed through the default hosted third-party gateway.

Mitigation: Use only non-sensitive creator identifiers and set SCRUMBALL_BASE_URL only to a trusted endpoint.

Risk: A durable local install identifier may tie repeated creator research activity to the same local environment.

Mitigation: Review before installing and delete ~/.scrumball_install_id if the local identifier needs to be reset.

Risk: Custom headers or API credentials may expose sensitive values if unnecessary headers are supplied.

Mitigation: Avoid passing custom headers unless required and keep SCRUMBALL_API_KEY out of shared logs or prompts.

## Reference(s):

- [API Index](artifact/references/api-index.md)
- [Request and Response Guide](artifact/references/request-response.md)
- [Operation Manifest](artifact/references/operations.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with fit scores, confidence, dimension-by-dimension breakdowns, API response summaries, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should include a fit score, score breakdown, go/test/no-go decision, and next validation action.]

## Skill Version(s):

1.0.2 (source: release evidence and config.yaml)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
