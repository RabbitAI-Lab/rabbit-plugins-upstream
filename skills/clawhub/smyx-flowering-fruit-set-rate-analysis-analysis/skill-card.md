## Description:

AI-powered tool that analyzes tomato or chili flower and fruit-cluster images or videos to count open flowers and young fruits, calculate fruit-set rate, and return a structured report with practical pollination and growing guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External growers, home gardening users, greenhouse operators, and agent workflows use this skill to analyze tomato or chili flower-cluster media, estimate flower and young-fruit counts, calculate fruit-set rate, and surface guidance for pollination and growing-condition adjustments.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Uploaded images, videos, and URL-sourced media are processed by configured LifeEmergence cloud services.

Mitigation: Use only media and URLs that are acceptable for cloud processing, and confirm the publisher's retention, account, and deletion controls before handling sensitive content.

Risk: The skill can silently create or reuse a persistent account identity and store generated identity and token data locally for report history.

Mitigation: Install in a workspace where persistent local identity storage is acceptable, review stored workspace data periodically, and avoid sharing workspaces across unrelated users.

Risk: Fruit-set analysis and recommendations may affect growing decisions but are derived from image or video quality and cloud model output.

Mitigation: Treat results as decision support, use clear close-range media, and have a human review important cultivation or production decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-flowering-fruit-set-rate-analysis-analysis)
- [Publisher profile](https://clawhub.ai/user/smyx-sunjinhui)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface notes](references/api_doc.md)
- [Shared analysis API notes](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, guidance]

**Output Format:** [Markdown or JSON structured analysis report with detected counts, fruit-set rate, recommendations, and report links.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save output to a file when requested; history lookup returns a structured report list from the configured cloud service.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter lists 1.0.10)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
