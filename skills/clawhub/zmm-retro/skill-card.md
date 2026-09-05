## Description:

A Chinese-language post-publish retrospective skill that collects short-video performance data, compares it with pre-publish predictions, attributes results through observable funnel metrics, and records validated lessons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[iamzifei](https://clawhub.ai/user/iamzifei)

### License/Terms of Use:

MIT-0

## Use Case:

External short-video creators use this skill after publishing a video to gather platform metrics, compare real outcomes with pre-release expectations, explain performance through observable funnel data, and preserve validated content lessons for future work.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may update local content memory and tracking files after drawing retrospective conclusions.

Mitigation: Review proposed file changes before accepting them, especially changes that deprecate prior lessons or add cross-skill memory.

Risk: A single video's metrics can be overgeneralized into durable content rules.

Mitigation: Keep first-time signals as hypotheses and promote them only after repeated validation, matching the skill's n=1 handling.

Risk: Required local zmm reference files may be unavailable, weakening the workflow's stated constraints.

Mitigation: Stop and disclose missing required references instead of substituting memory or assumptions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/iamzifei/skills/zmm-retro)

## Skill Output:

**Output Type(s):** [text, markdown, guidance, configuration]

**Output Format:** [Markdown-oriented retrospective analysis with recommended file updates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose updates to local skill memory and tracking files after reviewing user-provided video metrics.]

## Skill Version(s):

0.2.4 (source: server release evidence; artifact frontmatter states 0.1.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
