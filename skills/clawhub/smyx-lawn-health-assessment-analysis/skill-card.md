## Description:

Assesses top-down lawn images or videos to estimate yellowed turf, weed coverage, bare soil, and an overall lawn health score for maintenance planning.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External groundskeepers, golf-course teams, municipal greenway managers, and property managers use this skill to assess lawn condition from top-down media and guide irrigation, fertilization, weeding, or reseeding decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends lawn media or media URLs to lifeemergence.com services for analysis.

Mitigation: Use only with imagery approved for third-party cloud processing, and avoid sensitive property media unless the deployment has reviewed the service relationship.

Risk: The skill creates or reuses a local backend identity and stores backend tokens in a workspace SQLite database.

Mitigation: Run it in a dedicated workspace on shared machines and remove local state according to the operator's data-retention process.

Risk: Server security evidence notes mismatched pet/video analysis code and documentation.

Mitigation: Verify corrected publisher documentation and test expected lawn-analysis behavior before relying on production results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-lawn-health-assessment-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API reference](references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown or JSON text from CLI/API-backed analysis reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include structured lawn-health metrics, maintenance guidance, historical report tables, and report links.]

## Skill Version(s):

1.0.8 (source: server release evidence; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
