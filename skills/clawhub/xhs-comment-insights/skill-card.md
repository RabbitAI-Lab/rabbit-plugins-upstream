## Description:

Analyzes Xiaohongshu comments from a user-provided note link or note_id to extract themes, user feedback, pain points, purchase concerns, FAQs, reputation signals, and actionable insights for content, product, brand, and creator research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, product researchers, brand researchers, and creators use this skill to collect and summarize Xiaohongshu comment feedback into themes, pain points, purchase concerns, FAQs, and action recommendations. It supports bounded or paginated review of comments and replies from a supplied Xiaohongshu note URL, complete note_id, or comment_id.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Using the skill sends the supplied Xiaohongshu URL or IDs, pagination tokens, and the user's SocialDataX API key to SocialDataX-hosted services.

Mitigation: Install and run the skill only when that data transfer is acceptable, and keep SOCIALDATAX_API_KEY in the user's environment instead of embedding it in skill files or prompts.

Risk: Unbounded collection can occur when using the all-pages option.

Mitigation: Use bounded collection controls such as --pages or --max-items when a limited sample is sufficient.

Risk: Comment insights may overstate coverage when only the first page or a partial set of replies was collected.

Mitigation: State the collection scope in the output and distinguish returned comment text from inferred themes or recommendations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-comment-insights)
- [SocialDataX AI homepage](https://socialdatax.com/ai?from=clawhub)
- [ClawHub publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown summaries with optional shell command examples and JSON-derived evidence notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should state the comment coverage used, separate visible comment evidence from analysis, and avoid treating partial samples as full-platform coverage.]

## Skill Version(s):

0.1.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
