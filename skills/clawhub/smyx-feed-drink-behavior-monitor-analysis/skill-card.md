## Description:

Analyzes fixed-camera videos of feeders and waterers to quantify livestock feeding duration, feeding bouts and drinking frequency, comparing them against individual baselines to raise behavior anomaly alerts. | 通过视频统计畜禽采食时长、饮水频次，异常时预警。

This skill is ready for commercial/non-commercial use.

## Publisher:

[18072937735](https://clawhub.ai/user/18072937735)

### License/Terms of Use:

MIT-0

## Use Case:

External farm operators, livestock managers, and developers use this skill to analyze fixed-camera feeder or waterer media for feeding duration, feeding bouts, drinking frequency, baseline deviations, and behavior anomaly alerts. The results are behavior statistics and alerts, not disease diagnosis or treatment advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends livestock media or media URLs to the Life Emergence cloud service for analysis.

Mitigation: Use only media approved for that service and avoid including unrelated sensitive footage before execution.

Risk: The skill can create or reuse a local identity and store service tokens in the workspace data directory.

Mitigation: Review and remove local identity and token data, including data/smyx-api-key.txt and workspace data records, when uninstalling or rotating identities.

Risk: Historical report queries read cloud records associated with the current identity.

Mitigation: Confirm the active identity before querying history and avoid sharing workspaces across users with different report access expectations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/18072937735/skills/smyx-feed-drink-behavior-monitor-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [API interface documentation](references/api_doc.md)
- [Shared analysis API documentation](skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON text, including structured analysis reports, historical report lists, and report links]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can save analysis output to a user-provided file path; historical report lists are formatted for human review.]

## Skill Version(s):

1.0.8 (source: server release evidence; artifact SKILL.md frontmatter says 1.0.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
