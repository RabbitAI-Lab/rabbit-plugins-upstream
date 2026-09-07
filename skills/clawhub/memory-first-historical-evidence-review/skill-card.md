## Description:

Historical debug review: read dated memory first, then narrow raw session evidence only where memory leaves a causal gap.

This skill is ready for commercial/non-commercial use.

## Publisher:

[nextaltair](https://clawhub.ai/user/nextaltair)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to answer questions about earlier runs by building dated timelines from curated memory, then checking raw session evidence only where causal claims remain unsupported.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Historical memory and raw session logs can contain sensitive project or conversation details.

Mitigation: Use the skill only where review of those sources is acceptable, narrow lookups by date, session id, or exact phrase, and avoid broad scans unless the scoped evidence leaves a material gap.

## Reference(s):


## Skill Output:

**Output Type(s):** [Analysis, Markdown, Guidance]

**Output Format:** [Markdown narrative with cited evidence and separated verified versus likely causes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
