## Description:

Helps analyze Xiaohongshu (XHS/RedNote) note comments and replies for audience feedback, sentiment themes, questions, and pain points.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Analysts, marketers, and other users can retrieve Xiaohongshu note comments and replies to summarize audience feedback, recurring questions, objections, and sentiment themes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The runtime instructions invoke an unpinned npm package with access to the user's paid API key.

Mitigation: Install only if the package and publisher are trusted; pin the package to a reviewed exact version and protect SOCIALDATAX_API_KEY.

Risk: Unbounded comment pagination can consume substantial API credits or produce incomplete results after an interruption.

Mitigation: Set explicit page or item limits, and report partial results while resuming from the returned pagination token when appropriate.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-comments)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries of comment themes; retrieved comment data is JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summaries should distinguish single-page from multi-page results and identify incomplete retrievals.]

## Skill Version(s):

0.1.17 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
