## Description:

Checks whether an image appears AI-generated and reports a confidence score from 0 to 1.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

People reviewing images use this skill to request an AI-generation confidence score for an image URL or a local image.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Image checks submit images to Qinghu, including local images encoded for submission.

Mitigation: Only check images approved for external sharing; avoid sensitive images unless their disclosure is authorized.

Risk: Setup may install or update npm or Node tooling and alter the host environment.

Mitigation: Review installation commands and use a sandboxed environment for sensitive work.

Risk: The service requires a Qinghu API token configured locally.

Mitigation: Prefer a session-scoped token or environment variable and keep the token out of shared files.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-ai-image-detect)
- [Qinghu qhkit package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API keys](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports an AI-generation confidence score between 0 and 1 and credits charged for paid checks.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
