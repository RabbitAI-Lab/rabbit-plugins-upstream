## Description:

Creates coordinated e-commerce marketing images and videos, including product galleries, detail-page visuals, promotional posters, and advertising clips.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

Merchants and marketers use this skill to plan and generate a coordinated set of product images, promotional graphics, and short advertising videos through LinkPix.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing or updating the external qhkit package can change the local runtime and run mutable third-party tooling.

Mitigation: Review the package before installation and prefer a trusted, preinstalled, pinned version.

Risk: The skill needs a LinkPix/qhkit API token, which could be exposed if pasted into chat or stored insecurely.

Mitigation: Provide credentials through a secure secret mechanism and avoid sharing or casually persisting tokens.

Risk: Batch asset generation may consume paid credits.

Mitigation: Estimate the total charge and obtain user approval before submitting generation jobs.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/linkpix-marketing-assets)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Image and video links]

**Output Format:** [Markdown with grouped asset links and credit totals]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Video jobs may return a task ID before the final asset is ready.]

## Skill Version(s):

0.1.7 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
