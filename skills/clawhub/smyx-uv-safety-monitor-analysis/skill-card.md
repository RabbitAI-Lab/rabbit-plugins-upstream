## Description:

Analyzes camera images or video for pets near an active UV disinfection area and returns safety alerts, recommendations, and reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

Pet owners and boarding-facility staff can submit camera media to check for pets in UV disinfection areas, review risk alerts, and retrieve prior reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Home camera media or supplied media URLs are sent to the publisher's cloud service.

Mitigation: Use only media and URLs you are comfortable uploading to that service; review the skill before installation.

Risk: The skill silently creates or reuses an identity and stores tokens in the workspace data directory.

Mitigation: Restrict access to the workspace data directory and review stored identity and token data before use.

Risk: Cloud report history is tied to that identity and can be queried with limited user control.

Mitigation: Use a dedicated identity and avoid submitting sensitive media unless cloud history retention is acceptable.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/smyx-sunjinhui/skills/smyx-uv-safety-monitor-analysis)
- [API documentation](artifact/references/api_doc.md)
- [Skill demonstration](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [Analysis, Safety guidance, Report links]

**Output Format:** [JSON or Markdown text]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Historical report listings are available on request.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata; artifact frontmatter lists 1.0.19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
