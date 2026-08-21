## Description:

Generates customer-service reply drafts for cross-border ecommerce buyer messages on Amazon, Shopify, and TikTok Shop.

This skill is ready for commercial/non-commercial use.

## Publisher:

[metahuan](https://clawhub.ai/user/metahuan)

### License/Terms of Use:

MIT-0

## Use Case:

External ecommerce sellers and support agents use this skill to draft buyer-message replies for logistics questions, refunds, product issues, and presales inquiries while preserving platform-specific messaging constraints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Buyer messages and optional order, tracking, or product context may be sent to Yufluent's cloud service.

Mitigation: Provide only the information needed to draft the reply and avoid unnecessary personal data or sensitive order details.

Risk: Broad trigger wording could cause the skill to run for ambiguous customer-service requests.

Mitigation: Confirm the platform, language, buyer message, and intended reply task before invoking the cloud call.

Risk: Generated replies may contain inaccurate commitments if the supplied order context is incomplete or wrong.

Mitigation: Have the seller review the draft against actual order records and remove unsupported promises before sending.

Risk: The runtime dependency is specified as requests>=2.31.0 without an upper bound or lockfile.

Mitigation: Use a pinned, patched dependency set in controlled environments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/metahuan/skills/yufluentcn-chat-assist)
- [Yufluent chat-assist homepage](https://www.changzhiai.com/skills/chat-assist)
- [OpenClaw integration](https://claw.changzhiai.com/app/openclaw)

## Skill Output:

**Output Type(s):** [text, shell commands, guidance]

**Output Format:** [Plain text reply draft, with optional CLI usage guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reply drafts are intended for human review before sending through seller support channels.]

## Skill Version(s):

1.1.3 (source: server release evidence; artifact frontmatter reports 1.1.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
