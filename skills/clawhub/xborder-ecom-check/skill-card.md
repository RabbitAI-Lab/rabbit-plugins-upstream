## Description:

Checks cross-border e-commerce compliance across customs, product safety, consumer protection, VAT/GST, advertising, and data privacy, with offline preview and optional cloud scoring through compliancehub.cn.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wwumit](https://clawhub.ai/user/wwumit)

### License/Terms of Use:

MIT-0

## Use Case:

External sellers, marketplace operators, and compliance teams use this skill to preview a 12-item cross-border e-commerce checklist and generate scored compliance reports for destination-market obligations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scored runs send compliance-check answers to compliancehub.cn.

Mitigation: Use the non-interactive preview modes for offline review, and run scored checks only when the user accepts the cloud scoring data flow.

Risk: The skill uses local trial/API-key state for quota and authentication.

Mitigation: Keep API keys in COMPLIANCEHUB_API_KEY or a 0600 key file, and avoid entering sensitive business details beyond the requested pass/fail/na answers.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/wwumit/skills/xborder-ecom-check)
- [CQDev compliance cloud](https://compliancehub.cn)

## Skill Output:

**Output Type(s):** [text, json, html, files, guidance]

**Output Format:** [Plain text, JSON, or HTML compliance reports with recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scored runs may write a local report file when an output path is provided; preview modes list the bundled checklist offline.]

## Skill Version(s):

1.2.2 (source: evidence.json release and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
