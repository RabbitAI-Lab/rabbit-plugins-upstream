## Description:

Classify customer micro-moments into Buy Now, Research, Frustration, Advocacy, or Churn Risk with confidence scores.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ncreighton](https://clawhub.ai/user/ncreighton)

### License/Terms of Use:

MIT-0

## Use Case:

Customer support, customer success, sales, and marketing teams use this skill to classify customer messages across channels, review confidence scores, and choose routing or follow-up actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Customer communications may include sensitive or personal data that could be sent to OpenAI, Slack, CRM, or automation platforms.

Mitigation: Require clear consent, redact PII before processing, define retention rules, and confirm data-handling approvals before customer-facing use.

Risk: Intent classifications and routing recommendations can be wrong, especially for ambiguous messages or low confidence scores.

Mitigation: Run the skill in recommendation-only mode with manual review for low-confidence or high-impact customer actions.

Risk: Automated CRM or messaging workflows could trigger inappropriate outreach if classifications are used without approval gates.

Mitigation: Use explicit approval gates, audit logging, and human-controlled outreach before integrating with Slack, CRM, or automation tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ncreighton/skills/micro-moment-intent-classifier)
- [OpenAI API key setup](https://platform.openai.com/account/api-keys)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, guidance, configuration]

**Output Format:** [Markdown guidance with optional JSON, CSV, and dashboard-style summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include intent buckets, confidence scores, secondary intents, key phrases, reasoning, and recommended next actions.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
