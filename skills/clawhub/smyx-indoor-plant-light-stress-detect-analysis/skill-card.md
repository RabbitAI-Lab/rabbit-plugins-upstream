## Description:

Detects and analyzes indoor plant light stress from images and optional lux data, identifying low or excessive light symptoms and suggesting adjustments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze indoor plant images or videos, optionally with lux readings, for light stress classification and care adjustment guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends plant images or videos, URLs, report metadata, and an automatically selected user identity to the publisher's remote service.

Mitigation: Review before installation and use only when sharing those inputs with the publisher's service is acceptable.

Risk: The skill may create a local database containing reusable tokens.

Mitigation: Run in a controlled workspace and remove or protect the local data store according to the deployment's credential-handling policy.

Risk: Development/private HTTP endpoint configuration is present in the artifact.

Mitigation: Ask the publisher to correct or explain endpoint configuration before normal use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-indoor-plant-light-stress-detect-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API interface documentation](artifact/references/api_doc.md)
- [Shared analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)
- [Skill usage demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, guidance]

**Output Format:** [Markdown or JSON analysis report with care suggestions and report links; optionally saved to a local output file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include remote report links and historical report listings when requested.]

## Skill Version(s):

1.0.9 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
