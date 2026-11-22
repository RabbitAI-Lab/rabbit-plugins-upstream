## Description:

This skill provides a paid short-text generation workflow that creates an order, processes payment, and returns generated text after payment verification.

This skill is ready for commercial/non-commercial use.

## Publisher:

[laoguihui09-cmyk](https://clawhub.ai/user/laoguihui09-cmyk)

### License/Terms of Use:

MIT-0

## Use Case:

External users ask an agent to generate a short text from a topic or requirement after completing the required paid order flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security evidence says prompts and payment credentials are sent to web.kihb.shop with weak scoping.

Mitigation: Use only for non-sensitive prompts and payment credentials that are acceptable to share with the third-party service.

Risk: The security evidence says order records are stored locally and order-number validation is weak.

Mitigation: Review local order files before reuse, restrict access to the orders directory, and avoid relying on unvalidated order numbers.

Risk: The security evidence flags a reasoning-disclosure instruction in the artifact.

Mitigation: Remove or override requests to reveal reasoning before deploying the skill in production agent workflows.

Risk: The security evidence notes that the clawtip dependency and data-retention behavior are not clearly documented.

Mitigation: Document the payment dependency and retention expectations before offering the workflow to users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/laoguihui09-cmyk/skills/scripts)
- [Service website](https://web.kihb.shop)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Plain text with payment status messages]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a paid order and payment credential before service execution.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
