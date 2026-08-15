## Description:

Assesses top-down lawn images or videos to estimate yellowing, weed coverage, bare soil, a 0-100 health score, and care recommendations through a configured cloud analysis service.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External grounds managers, municipal landscaping teams, sports-field staff, golf-course staff, and homeowners use this skill to evaluate lawn imagery for yellowing, weed density, bare soil, and maintenance direction.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lawn images or videos, media URLs, and account-linked report history are sent to the configured cloud service.

Mitigation: Install only if the publisher is trusted, avoid sensitive property imagery, and use a separate workspace when possible.

Risk: The skill stores local identity and token state for reuse.

Mitigation: Review or clear data/smyx-common-claw.db and data/smyx-api-key.txt if persistent identity or token reuse is not wanted.

Risk: History-report queries retrieve cloud report history beyond a single image assessment.

Mitigation: Use history queries only when account-linked cloud report retrieval is expected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-lawn-health-assessment-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [API interface reference](references/api_doc.md)
- [Common analysis API reference](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON analysis report with metrics, recommendations, report links, and optional saved result file.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts a local lawn image/video file path or public media URL; documented formats include jpg, png, mp4, avi, and mov with a 10 MB maximum file size.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
