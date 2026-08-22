## Description:

青虎AI 电影质感 TVC 广告大片 helps an agent collect product images and campaign details, estimate cost, request user approval, and submit a Qinghu AI workflow that generates a cinematic product advertising video.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing teams, creators, and agent operators use this skill to turn 1 to 8 authorized product images plus product, audience, scene, style, language, and aspect-ratio choices into a polished TVC-style advertising video through Qinghu AI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The workflow can spend Qinghu credits when generation is submitted.

Mitigation: Run the estimate action first, present the estimated credit cost and key parameters, and submit only after explicit user approval.

Risk: The workflow uploads user-provided product images to a third-party Qinghu AI service.

Mitigation: Use only images the user owns or is authorized to process, and disclose the upload before generation.

Risk: The qhkit CLI may require a Qinghu API token or local configuration.

Mitigation: Treat tokens as credentials, use the documented qhkit configuration path or environment variable, and avoid exposing token values in user-facing output.

Risk: Generated ad scripts or visuals may include claims that need legal or brand review.

Mitigation: Ask the user to verify advertising claims, product benefits, and compliance-sensitive wording before using the generated video commercially.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/autoagc/skills/qinghu-tvc-ad-film)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API Keys](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration, markdown]

**Output Format:** [Markdown guidance with JSON and bash command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guides qhkit workflow options, estimate, generate, and status commands; final media is returned by the Qinghu workflow as video URLs such as primaryVideo.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
