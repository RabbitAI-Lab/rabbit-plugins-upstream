## Description:

AI-powered lawn health assessment from drone or fixed-camera top-down images that estimates wilting or yellow turf, weed coverage, bare soil, and a composite lawn health score.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and turf managers use this skill to assess top-down lawn images or videos for wilting ratio, weed density, bare-soil coverage, health score, and practical maintenance direction. It is aimed at home yards, golf courses, municipal park lawns, greenways, and sports fields.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends lawn images, videos, or supplied URLs to a configured external service.

Mitigation: Use only non-sensitive imagery or obtain appropriate consent before analysis, and review the configured service endpoints before deployment.

Risk: The skill can automatically create or reuse an internal account identity and store identity tokens in a local workspace database.

Mitigation: Review local workspace data handling, restrict filesystem access to the workspace data directory, and clear stored tokens when the skill is removed or reassigned.

Risk: The bundled configuration includes development settings and under-scoped network behavior flagged by the authoritative scan.

Mitigation: Remove or replace development configuration before production use and allow only approved production endpoints.

Risk: Cloud report-history queries may expose prior analysis records associated with the resolved account identity.

Mitigation: Limit use of report-history commands to authorized users and verify that the resolved account identity matches the intended user or workspace.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-lawn-health-assessment-analysis)
- [API interface reference](references/api_doc.md)
- [Shared analysis API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown and JSON-like structured analysis text, with optional saved output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and cloud report-history listings when the configured service returns them.]

## Skill Version(s):

1.0.9 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
