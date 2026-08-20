## Description:

Cross-border paid ads optimization coach across targeting, creatives, bidding, landing page, and analytics for Meta, TikTok, Google, and multi-channel campaigns via the Yufluent cloud Harness.

This skill is ready for commercial/non-commercial use.

## Publisher:

[metahuan](https://clawhub.ai/user/metahuan)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to collect advertising context and metrics, call the Yufluent cloud service, and receive optimization guidance for audience targeting, creative testing, bidding, landing pages, and analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ad metrics, campaign context, and TOKENAPI_KEY are sent to Yufluent's cloud service.

Mitigation: Review sensitive business metrics before submission and protect TOKENAPI_KEY as a secret.

Risk: Advertising recommendations may be incorrect, incomplete, or unsuitable for a target market or platform policy.

Mitigation: Require human review before applying recommendations in advertising platforms and check applicable platform policies and local regulations.

Risk: The dependency declaration allows a version range for requests.

Mitigation: Pin and review dependencies in controlled environments before deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/metahuan/skills/yufluentcn-ad-optimize)
- [Yufluent ad optimization homepage](https://www.changzhiai.com/skills/ad-optimize)
- [OpenClaw integration](https://claw.changzhiai.com/app/openclaw)
- [Yufluent console](https://claw.changzhiai.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or plain text returned from the cloud skill, with CLI commands and optional JSON inputs for structured metrics.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires TOKENAPI_KEY; accepts campaign message, optimization dimension, ad platform, product, market, metrics, context, and language.]

## Skill Version(s):

1.1.3 (source: server release metadata; artifact frontmatter lists 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
