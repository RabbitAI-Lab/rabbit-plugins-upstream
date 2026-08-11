## Description:

Analyzes cat tree videos or URLs through server-side APIs to report layer dwell time, jumps or transitions, and a 2D activity heatmap for activity and enrichment observation, without diagnosing disease.

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to analyze cat climbing frame or cat tree footage, quantify where a pet spends time, count jumps or transitions, and produce an activity heatmap report for enrichment and activity monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet videos or URLs are processed by external lifeemergence.com APIs.

Mitigation: Avoid private home camera footage unless the publisher provides clear retention and deletion terms, and review the API terms before deployment.

Risk: The skill silently creates or reuses an internal identity, sends that identity to a login endpoint, and stores returned service tokens in a local shared SQLite database.

Mitigation: Run the skill in an isolated environment, review account-linking behavior, and restrict access to local token storage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-pet-climbing-frame-heatmap-analysis)
- [API documentation](references/api_doc.md)
- [SMYX analysis API documentation](skills/smyx_analysis/references/api_doc.md)
- [Skill demo](https://lifeemergence.com/sample.html)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown reports and JSON text returned by shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include report links and saved result files when --output is used.]

## Skill Version(s):

1.0.7 (source: server release metadata; artifact frontmatter reports 1.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
