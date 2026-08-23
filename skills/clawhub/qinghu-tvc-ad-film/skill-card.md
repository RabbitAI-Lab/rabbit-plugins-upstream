## Description:

Guides an agent through Qinghu AI's paid workflow for creating cinematic TVC brand advertising videos from 1-8 product images plus product, audience, scene, style, language, and aspect-ratio fields.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, marketers, and agents use this skill to prepare, estimate, confirm, submit, monitor, and deliver Qinghu AI TVC advertising-video jobs. It is intended for product-ad generation workflows where the user provides authorized product images and campaign details.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can initiate a paid TVC generation workflow that consumes Qinghu credits.

Mitigation: Run an estimate first, summarize the exact submitted fields and expected credit cost, and wait for explicit user approval before calling generate.

Risk: The skill may require global npm, Node, Pillow, or npx-based setup and access to API credentials.

Mitigation: Review installation commands before execution and provide Qinghu API tokens only through the intended secure configuration path or environment variable.

Risk: Submitted product images and advertising claims may create copyright, authorization, or commercial-compliance issues.

Mitigation: Use only owned or licensed product assets and have the user review claims, audience targeting, and final ad copy before commercial use.

Risk: Online workflow fields and options can change after the artifact's documented snapshot.

Mitigation: Query the live workflow options before submission and copy field labels and option values exactly from the returned data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-tvc-ad-film)
- [Publisher profile](https://clawhub.ai/user/autoagc)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key console](https://www.iqinghu.com/workbench/dashboard/api-keys)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with bash commands and JSON parameter examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The guided CLI workflow returns one-line JSON status and, when generation succeeds, generated video URLs.]

## Skill Version(s):

0.1.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
