## Description:

Guides an agent in turning documents into explainer, report, courseware, or training videos through the dLazy document-to-video service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Creators, educators, and business users can use this skill to prepare explainer, report, courseware, and training videos from Word, PDF, presentation, spreadsheet, or Markdown documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes an external CLI and hosted service.

Mitigation: Review the @dlazy/cli package and dLazy service terms before installing or using it.

Risk: Using the service can save an API key locally and upload attached documents to dLazy-hosted services.

Mitigation: Protect the local API key and obtain approval before uploading sensitive documents.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/dlazyai/skills/dlazy-doc-to-video)
- [dLazy CLI source listed in skill metadata](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy service](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Plain text or Markdown with shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The hosted service handles video creation; the agent receives project-scoped replies and may provide generated video results.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
