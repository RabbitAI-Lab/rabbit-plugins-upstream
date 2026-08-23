## Description:

Detects estrus behavior in female livestock from continuous barn videos, including mounting acceptance, standing reflex, restlessness, appetite drop and vulva changes, and outputs an estrus recognition result with an optimal mating time window.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External livestock operators and developers use this skill to analyze fixed-camera barn images or video for female livestock estrus indicators, estrus-stage classification, optimal mating-window timing, and historical report lookup. Results are intended as a visual behavior reference and should be reviewed with farm procedures and qualified breeding staff before operational decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Barn images, videos, or media URLs may be uploaded to a remote API for analysis.

Mitigation: Review data handling expectations with the publisher and test with non-sensitive media before using production farm footage.

Risk: The skill may silently create or reuse a backend identity and persist tokens in a local workspace database.

Mitigation: Run it in an isolated workspace, review local credential storage, and clear generated identity or token state between users or environments.

Risk: The packaged development configuration references a private API endpoint.

Mitigation: Verify or replace API endpoint configuration before deployment and confirm only intended production services are reachable.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-estrus-mating-behavior-detect-analysis)
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill Demo](https://lifeemergence.com/sample.html)
- [API Interface Documentation](references/api_doc.md)
- [Analysis API Documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json]

**Output Format:** [Markdown tables or JSON analysis reports with report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local image/video paths or media URLs; supports basic, standard, and json detail levels.]

## Skill Version(s):

1.0.9 (source: server release metadata; SKILL.md frontmatter lists 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
