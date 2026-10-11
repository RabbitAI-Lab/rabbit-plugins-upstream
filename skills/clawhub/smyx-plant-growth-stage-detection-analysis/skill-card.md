## Description:

Analyzes plant images or videos to identify growth stages and phenological features, report confidence, and offer general care guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Gardeners, growers, and greenhouse operators use plant images or videos to assess growth stage and view general care guidance. They can also request prior analysis reports from the cloud service.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Plant images, videos, or supplied URLs are sent to an external cloud service for analysis.

Mitigation: Review the service's data-handling terms and obtain consent before sending sensitive media or URLs.

Risk: The skill may create or reuse a local identity, query cloud report history, and retain service tokens in a workspace database.

Mitigation: Review account creation and token retention before installing; restrict access to the workspace and stored credentials.

Risk: The bundled Python code changes its import path, which may cause unintended modules to be loaded.

Mitigation: Review the code and its dependencies before execution; prefer a release that removes the import-path workaround.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-growth-stage-detection-analysis)
- [Plant growth stage API documentation](references/api_doc.md)
- [Skill usage introduction](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Text or Markdown analysis report; optional JSON output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Growth-stage assessment, confidence, general care guidance, and report links; optional cloud report history.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata; bundled SKILL.md lists 1.0.17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
