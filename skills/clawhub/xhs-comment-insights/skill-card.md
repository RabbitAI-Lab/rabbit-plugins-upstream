## Description:

Analyzes Xiaohongshu/XHS comment data from user-provided note URLs or complete note IDs to summarize user feedback, pain points, purchase concerns, FAQs, reputation signals, replies, and discussion themes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content operations, product research, brand research, and customer support teams use this skill to collect and analyze comments and replies from a specific Xiaohongshu/XHS note. It turns returned comments into themes, pain points, purchase objections, FAQs, representative quotes, and actionable follow-up ideas while stating the sampled input scope.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill invokes a third-party SocialDataX integration and npm package.

Mitigation: Before installing or running it, confirm the user trusts SocialDataX and the socialdatax-skills package.

Risk: Provided Xiaohongshu note IDs or URLs are sent to SocialDataX using the user's SOCIALDATAX_API_KEY.

Mitigation: Use the skill only with inputs the user is comfortable sending to SocialDataX, and keep the API key in the runtime environment rather than embedding it in files.

Risk: Broad pagination options such as --all may consume more API credits than expected.

Mitigation: Prefer --pages or --max-items limits while exploring, and expand pagination only when the user wants broader coverage.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-comment-insights)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Guidance]

**Output Format:** [Markdown analysis with optional shell command examples and JSON CLI/API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only; requires SOCIALDATAX_API_KEY and may paginate comments or replies when requested.]

## Skill Version(s):

0.1.4 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
