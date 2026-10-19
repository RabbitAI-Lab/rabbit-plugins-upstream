## Description:

Helps content planners turn current Xiaohongshu hot-search trends and sampled popular notes into actionable topic ideas.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators and marketing teams use current Xiaohongshu hot-search signals and sampled public notes to prioritize topics, develop title hooks, and identify trends to skip.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The suggested command runs the latest, unpinned npm release with a SocialDataX API key.

Mitigation: Review the package and prefer a pinned version before running it with the key.

Risk: Xiaohongshu search terms are sent to SocialDataX.

Mitigation: Avoid sending sensitive topics unless this external data sharing is acceptable.

Risk: Returned note URLs may contain xsec_token values that the skill preserves in output.

Mitigation: Avoid storing or forwarding those URLs beyond what is needed for the analysis.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/xhs-hot-topic-selection)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown topic analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Summarizes current hot-list signals and sampled notes, with topic candidates, title hooks, content angles, and next steps; coverage is limited to returned results.]

## Skill Version(s):

0.1.9 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
