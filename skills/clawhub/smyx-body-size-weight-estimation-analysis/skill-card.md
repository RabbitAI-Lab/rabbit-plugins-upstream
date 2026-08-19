## Description:

Estimates livestock body length and body weight from side-view videos or frames, tracking fattening progress in a contactless manner.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agricultural operators use this skill to estimate livestock body dimensions, weight, and fattening stage from side-view images, videos, local files, or URLs. It supports contactless monitoring workflows and historical report lookup while treating estimates as reference information rather than feeding or sale advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Livestock media, private URLs, internal identity values, and report history may be sent to the configured external service.

Mitigation: Review the configured service and only run the skill with media, URLs, and report data approved for that service.

Risk: The skill may create or reuse a local account identity and store returned authentication tokens in a shared workspace database.

Mitigation: Use an appropriate workspace boundary, review local token storage before shared deployments, and rotate or remove stored tokens when access should end.

Risk: Body size, weight, and fattening-stage estimates can be affected by image quality, side-view pose, occlusion, reference-object calibration, and video stability.

Mitigation: Require clear side-view capture with a known-size reference object and treat results as monitoring references rather than definitive weighing or sale decisions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-body-size-weight-estimation-analysis)
- [API Documentation](references/api_doc.md)
- [Skill Demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports, JSON analysis output, report links, and command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include estimated body length, body height, chest or body width, weight, fattening stage, confidence or usability notes, and historical report tables.]

## Skill Version(s):

1.0.9 (source: server release evidence, released 2026-08-17T15:22:32Z)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
