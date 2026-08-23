## Description:

Assesses post-grooming pet images or videos for mat residue, dandruff coverage, coat smoothness, and a 0-100 grooming score with re-grooming suggestions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, groomers, and salon quality reviewers use this skill to evaluate grooming completeness from pet media and identify when additional brushing or care may be needed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet images, videos, and report queries are sent to the publisher's remote backend.

Mitigation: Install only where this data flow is acceptable, and review user notice, endpoint ownership, and retention expectations before deployment.

Risk: The skill silently creates or reuses account identity and stores generated identity and tokens in a local workspace database.

Mitigation: Limit workspace access, clear local state when no longer needed, and review token handling before shared or production use.

Risk: Security evidence flags default dev or private HTTP configuration as needing correction or explanation before production use.

Mitigation: Correct the configuration to approved production endpoints or document why each non-production endpoint is acceptable before release.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-grooming-effect-assessment-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API 接口文档](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown reports and JSON analysis results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can write an output report file when requested; history lists are rendered as Markdown tables.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter reports 1.0.11)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
