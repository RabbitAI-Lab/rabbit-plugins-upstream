## Description:

This skill helps agents use Qinghu AI to generate door-opening outfit-change videos from one model image, up to four clothing images, and optional audio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, ecommerce teams, and agents use this skill to prepare and run Qinghu AI outfit-change video jobs for women's fashion try-on and product video workflows. It guides setup, parameter preparation, cost estimation, paid submission, polling, and delivery of generated media URLs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Paid generation can consume Qinghu credits and submitted jobs may not be cancelable.

Mitigation: Run an estimate with the same parameters, show the expected credit cost and key inputs, and wait for explicit user approval before generating.

Risk: Using model, outfit, or audio assets without rights can create authorization and commercial-use issues.

Mitigation: Use only assets the user owns or is authorized to process, and confirm model likeness rights before submission.

Risk: Qinghu workflow fields and labels may change after the documented snapshot.

Mitigation: Run the workflow options command when uncertain and use the returned field labels exactly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-door-outfit-change)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys)
- [ClawHub publisher profile](https://clawhub.ai/user/autoagc)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Markdown]

**Output Format:** [Markdown with inline bash and JSON examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can include qhkit workflow commands, parameter JSON, status polling guidance, and generated media URLs when jobs complete.]

## Skill Version(s):

0.1.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
