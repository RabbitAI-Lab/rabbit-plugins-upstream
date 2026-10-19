## Description:

Analyzes Douyin comments and replies with SocialDataX to summarize audience feedback, sentiment themes, objections, and frequently asked questions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content teams and analysts use this read-only skill to examine Douyin comments and replies for audience feedback, recurring questions, sentiment themes, and pain points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The latest npm package version may change between runs.

Mitigation: Use a reviewed, pinned package version or a managed MCP tool where reproducibility is required.

Risk: The SocialDataX service and its npm package receive access to the configured API key.

Mitigation: Verify that you trust both providers before setting SOCIALDATAX_API_KEY.

Risk: Unbounded pagination or partial replies can yield unexpectedly large or incomplete analyses.

Mitigation: Set page or item limits when appropriate, and label partial results and reply coverage clearly.

## Reference(s):

- [SocialDataX API access and product information](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-comments)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown analysis or summaries based on JSON comment data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Report page coverage and clearly identify partial results.]

## Skill Version(s):

0.1.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
