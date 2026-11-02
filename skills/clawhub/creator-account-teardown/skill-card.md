## Description:

Analyzes a creator account’s positioning, audience, content patterns, and cadence, then develops an account plan and a produced first post with a cover and narration.

This skill is ready for commercial/non-commercial use.

## Publisher:

[beatra-ai](https://clawhub.ai/user/beatra-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators and social-media teams use the skill to benchmark an account, understand its positioning and recurring content patterns, and turn those findings into a plan for their own account. It can also draft and produce a first post with a rendered cover and narration.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The connection grants broader shared Beatra access than this workflow needs and enables recurring installation analytics.

Mitigation: Review the requested access before connecting, prefer a release with narrower permissions, and revoke the shared connection in the Beatra Console when needed.

Risk: A cleanup flaw may disconnect other Beatra skills that share the connection.

Mitigation: Prefer a release with corrected uninstall validation and check the impact on other Beatra skills before disconnecting.

Risk: Account lookups and content-production requests may incur charges, and uploads send selected files for processing.

Mitigation: Review and approve each request at its stated price, and upload only files intended for processing.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/beatra-ai/skills/creator-account-teardown)
- [Beatra skill homepage](https://beatra.ai/skills/creator-account-teardown)
- [Account lookup guidance](artifact/references/account-lookup.md)
- [Account teardown workflow](artifact/references/workflow.md)
- [Build-template guidance](artifact/references/build-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Markdown, Image, Audio]

**Output Format:** [Structured written analysis and account plan, plus a rendered cover image and narrated first-post script when produced.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Analysis is based on supported account lookups or material supplied by the user; unsupported platforms must be assessed from user-provided material.]

## Skill Version(s):

0.2.5 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
