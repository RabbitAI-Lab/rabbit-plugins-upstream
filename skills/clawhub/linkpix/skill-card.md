## Description:

Helps agents create and edit ecommerce images and videos, draft advertising content, and query Qinghu ecommerce data through the qhkit tool.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Ecommerce marketers and content creators use this skill to plan and produce product images, promotional videos, storyboards, and advertising copy, and to research products and trends across ecommerce platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or upgrading an unpinned external npm package may introduce changed behavior.

Mitigation: Review the qhkit package and prefer a pinned, reviewed version before installation or upgrades.

Risk: The service receives an API key and uploaded media, including uploads that may occur during estimates.

Mitigation: Use a trusted account and upload only media approved for sharing with Qinghu; protect the API key.

Risk: Generating media or calling paid data tools can spend Qinghu credits.

Mitigation: Review estimated costs and parameters, then obtain explicit user confirmation before paid submissions.

Risk: Face edits, watermark removal, and copying third-party videos or creative may violate rights or consent.

Mitigation: Use these features only with appropriate rights and consent.

## Reference(s):

- [LinkPix on ClawHub](https://clawhub.ai/autoagc/skills/linkpix)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu workbench](https://www.iqinghu.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with commands, summaries, and links to generated media]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Generated images and videos are delivered as external links; paid tasks require confirmation and may need status checks.]

## Skill Version(s):

0.1.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
