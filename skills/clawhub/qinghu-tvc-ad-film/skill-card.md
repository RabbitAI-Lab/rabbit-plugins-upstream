## Description:

青虎AI 电影质感 TVC 广告大片 helps an agent collect product images and campaign fields, use Qinghu's qhkit workflow, and generate a cinematic TVC-style product advertising video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and marketing teams use this skill to turn 1 to 8 product images, product positioning, audience, scenario, language, and aspect-ratio choices into a hosted Qinghu AI TVC advertising workflow. Agents use it to check available fields, estimate credits, obtain user confirmation, submit the workflow, poll status, and return the generated video URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow uploads selected product images to Qinghu's hosted ad-generation service.

Mitigation: Use only product assets the user owns or is authorized to process, and confirm that upload to Qinghu is acceptable before submission.

Risk: The workflow requires Qinghu API credentials and local qhkit configuration.

Mitigation: Store credentials only through qhkit configuration or environment variables, avoid exposing tokens in shared logs, and report configuration errors without revealing secrets.

Risk: Submitting a generation consumes Qinghu credits after estimation and confirmation.

Mitigation: Run qhkit estimate with the final parameters, show the expected credit cost, and wait for explicit user approval before generate.

Risk: Generated advertising copy or video may contain claims that need business, legal, or platform review.

Mitigation: Have the user review the final ad for product-claim accuracy, rights clearance, and advertising compliance before publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tvc-ad-film)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with bash commands and JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return hosted workflow status and generated video URLs after qhkit completes.]

## Skill Version(s):

0.1.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
