## Description:

Routes short-drama and comic-drama projects through creator-led stages, with project setup, a local dashboard, production-form guidance, and project exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[worldwonderer](https://clawhub.ai/user/worldwonderer)

### License/Terms of Use:

MIT

## Use Case:

Creators use this skill to initialize or continue a short-drama project in a local filesystem, route work to the relevant creative stage, view project progress, and export current materials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security assessment is benign with medium confidence, but coverage is partial and the tool scope is undeclared, leaving uncertainty about permissions and behavior.

Mitigation: Review the skill's permissions and behavior before installation, and confirm its filesystem scope fits the intended project.

Risk: Fixed language defaults may not suit a project's needs.

Mitigation: Check the project's language and prompt-language settings before continuing creative work.

## Reference(s):

- [Creator-first workflow](references/creator-workflow.md)
- [Creator documents](references/creator-documents.md)
- [Production-form profiles](references/production-form-profiles.md)
- [Runtime preflight and safe writes](references/runtime-preflight.md)
- [Contract and ownership](references/contract-and-ownership.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Configuration, Shell commands]

**Output Format:** [Markdown project documents, JSON project configuration, and command-line instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates project materials and can provide a dashboard or export snapshot when requested; creative stages and media production may be routed to companion skills.]

## Skill Version(s):

1.0.36 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
