## Description:

Helps agents create and edit e-commerce images and videos, draft scripts, and retrieve marketplace data through Qinghu AI tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

E-commerce creators and marketing teams use this skill to produce product imagery, ads, videos and scripts, or analyze marketplace products, creators and trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad request triggers could route unrelated media or shopping tasks to an external service.

Mitigation: Use only when the user intends to use Qinghu for the requested task.

Risk: Installing an unpinned package may change the global tool environment.

Mitigation: Confirm installation or PATH changes first and prefer a reviewed, pinned qhkit version where possible.

Risk: API tokens and local media may be exposed to an external service, including during some estimates.

Mitigation: Protect the token, share only necessary files and confirm uploads before use.

Risk: Media generation and data calls may consume paid credits.

Mitigation: Review current credit estimates and obtain explicit approval before paid submissions.

## Reference(s):

- [青虎AI ClawHub release](https://clawhub.ai/autoagc/skills/qinghu-ai)
- [Qinghu qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu workbench](https://www.iqinghu.com)
- [Qinghu API key setup guide](https://xcnzsfe4uxrw.feishu.cn/wiki/KJ0Ywsyw8iAXmRkz5l4cddDbn6g)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, Media links, Marketplace data]

**Output Format:** [Markdown with media links, scripts and summarized data; tabular or JSON results when applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Media and data tasks may use paid credits; obtain a quote and approval before submitting.]

## Skill Version(s):

0.1.4 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
