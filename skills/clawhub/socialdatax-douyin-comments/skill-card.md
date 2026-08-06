## Description:

Helps agents retrieve and analyze Douyin first-level comments and comment replies for audience feedback, sentiment themes, objections, pain points, FAQs, and discussion summaries using SocialDataX.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to fetch Douyin comments or replies by content URL, aweme ID, or comment ID and summarize discussion themes, user feedback, sentiment signals, objections, pain points, and FAQs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires a SocialDataX API key in the runtime environment.

Mitigation: Provide the API key only through SOCIALDATAX_API_KEY and do not embed credentials in prompts, generated files, or command examples.

Risk: Examples invoke the latest published socialdatax-skills CLI package, so package behavior may change over time.

Mitigation: Review npm package updates before use and install only if the current SocialDataX package behavior is acceptable.

Risk: Incorrect Douyin URLs, aweme IDs, comment IDs, or pagination tokens can produce failed, incomplete, or mismatched comment retrieval.

Mitigation: Use Douyin content page URLs or known aweme IDs, keep opaque pagination tokens unchanged, and report whether one page or multiple pages were analyzed.

Risk: Repeated retries after insufficient-balance errors can waste time and obscure the required user action.

Mitigation: Do not repeatedly retry insufficient-balance errors; show the recharge URL returned by the service and continue only after the user recharges.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-comments)
- [ClawHub publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples; runtime SocialDataX tool output is JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and node/npm; generated outputs should state whether one or multiple pages of comments were analyzed.]

## Skill Version(s):

0.1.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
