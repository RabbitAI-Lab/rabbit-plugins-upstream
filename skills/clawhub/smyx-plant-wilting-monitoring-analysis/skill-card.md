## Description:

Early monitoring of plant wilting based on hyperspectral imaging and computer vision, captures early wilting signs before visible symptoms, provides early warning for precision irrigation and disease control.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agricultural developers use this skill to submit plant images, videos, or media URLs for early wilting monitoring, severity assessment, and report retrieval to support irrigation and disease-control decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can upload media or media URLs to a remote service and query cloud report history.

Mitigation: Use it only when remote analysis and cloud history retrieval are approved for the submitted plant media.

Risk: The skill can automatically create or reuse an account identity and store tokens in the workspace data area.

Mitigation: Review local identity and token storage before deployment, and clear stored state when deprovisioning or changing users.

Risk: The security evidence notes default non-HTTPS development endpoints.

Mitigation: Configure approved HTTPS production endpoints before use and reject private or non-HTTPS development endpoints in deployment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-plant-wilting-monitoring-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [JSON or Markdown text with analysis details, history rows, and report links depending on detail mode and list mode.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May upload local media or pass media URLs to a remote analysis service; history listing queries cloud reports for the resolved user identity.]

## Skill Version(s):

1.0.12 (source: server release metadata; artifact frontmatter states 1.0.14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
