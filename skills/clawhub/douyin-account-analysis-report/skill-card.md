## Description:

This skill helps agents analyze Douyin accounts from a profile link, share text, or sec_user_id and produce an evidence-based account diagnosis report using recent account and post data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users, content operators, and agents use this skill to collect Douyin account profile and recent-post data, then produce a structured diagnosis report with evidence-backed observations and a 30-day testing plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin profile links, share text, or account identifiers are sent to SocialDataX for analysis.

Mitigation: Use only account inputs the user intends to analyze and configure SOCIALDATAX_API_KEY through the runtime environment.

Risk: The report could overstate platform causality when playback, exposure, completion, or recommendation metrics are not returned.

Mitigation: Base conclusions only on returned public metrics and explicitly note missing metrics.

Risk: Analysis may be interrupted by missing Node.js/npm/npx, API-key configuration issues, network errors, or insufficient SocialDataX balance.

Mitigation: Check runtime prerequisites and SOCIALDATAX_API_KEY before use, retry non-balance API failures once, and preserve partial results when pagination or calls fail.

## Reference(s):

- [SocialDataX AI API](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/douyin-account-analysis-report)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown report with optional shell command examples and tabular account analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses only returned account and recent-post data; missing metrics should be called out rather than inferred.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
