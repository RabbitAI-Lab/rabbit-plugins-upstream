## Description:

Analyzes plant images or videos to estimate wilting severity and, when soil-moisture data is available, assess whether underwatering or waterlogging may be involved.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

Plant owners, gardeners, and greenhouse or plant-factory operators can submit a plant image or video to estimate wilting severity, consider possible causes, and receive general intervention guidance. Cause attribution is less certain without soil-moisture data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may silently enroll a service account and use a configured API secret as account identity data.

Mitigation: Defer installation until identity and credential handling are corrected and remote enrollment and token storage are explained. Rotate any API secret already configured and used.

Risk: The skill may submit media to the remote service despite an option that promises no analysis.

Mitigation: Defer installation until this behavior is corrected. Submit only media you are authorized to upload, and review service charges and retention terms.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/18072937735/skills/smyx-plant-wilting-quantification-analysis)
- [Skill demonstration](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Guidance]

**Output Format:** [Structured analysis report in JSON or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Wilting estimate (0–100%), possible cause, general intervention direction, and report link; cause attribution is uncertain without soil-moisture data.]

## Skill Version(s):

1.0.19 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
