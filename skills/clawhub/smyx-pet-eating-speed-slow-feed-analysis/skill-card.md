## Description:

Analyzes pet food-bowl videos or video URLs through cloud APIs to estimate feeding duration and speed, produce structured reports and report links, and suggest slow-feeding interventions without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External pet-care users and developers use the skill to submit local or network feeding videos for eating-speed analysis, slow-feed intervention recommendations, and cloud history report retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet or home feeding videos, video URLs, and account-linked identity data are sent to configured Lifeemergence cloud services.

Mitigation: Use the skill only with videos and account contexts approved for those cloud services.

Risk: The skill may create a local workspace database that caches tokens and retrieves prior reports automatically.

Mitigation: Review local workspace storage and token handling before deployment, and clear cached data when it is no longer needed.

Risk: The security scanner marked the release suspicious because identity, local tokens, and cloud history are handled silently.

Mitigation: Require an installation review focused on identity handling, token storage, and cloud history access.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-eating-speed-slow-feed-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet eating speed API documentation](artifact/references/api_doc.md)
- [Common analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, guidance]

**Output Format:** [Markdown and JSON analysis reports with report links and optional saved output files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports local video files, video URLs, pet type selection, report detail levels, and historical report listing.]

## Skill Version(s):

1.0.8 (source: server release metadata; artifact frontmatter says 1.0.9)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
