## Description:

This skill helps an agent prepare, quote, submit, monitor, and deliver Qinghu AI cinematic TVC advertising video jobs from user-provided product images and campaign details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill when they need an agent to generate product-focused TVC ad videos through Qinghu AI, including collecting required inputs, confirming credit cost, submitting the workflow, polling status, and returning completed media links.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow spends Qinghu credits when a generation job is submitted.

Mitigation: Run an estimate first, present the quoted credit cost and key parameters to the user, and submit only after explicit user confirmation.

Risk: The workflow uploads user-provided product images to Qinghu AI for processing.

Mitigation: Use only images the user owns or is authorized to process, and disclose that the qhkit workflow sends those assets to the service.

Risk: Generated ad videos and ad copy may contain claims that require commercial or regulatory review.

Mitigation: Ask the user to review factual claims, product benefits, and compliance-sensitive language before publishing or using the ad.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tvc-ad-film)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu AI site](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Markdown]

**Output Format:** [Markdown guidance with qhkit shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include quote-confirmation text, workflow status handling, and final media URL delivery guidance.]

## Skill Version(s):

0.1.3 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
