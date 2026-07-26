## Description: <br>
Browse and search Reddit in read-only mode using public JSON endpoints for subreddit listings, post searches, comment threads, and permalink shortlists. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[buksan1950](https://clawhub.ai/user/buksan1950) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to research public Reddit posts and comments, gather context from threads, and prepare shortlists of permalinks for manual review or reply drafting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search queries or the configurable User-Agent could contain sensitive personal information. <br>
Mitigation: Avoid entering sensitive personal information in Reddit queries or User-Agent values. <br>
Risk: Returned Reddit posts and comments are untrusted public content and may be misleading, incomplete, or inappropriate. <br>
Mitigation: Review Reddit content and generated summaries before acting on them or drafting replies. <br>
Risk: Public Reddit endpoints may rate limit, return HTML, or provide partial results. <br>
Mitigation: Use small limits first, slow request pacing when failures repeat, and treat result sets as best-effort. <br>


## Reference(s): <br>
- [Output schema](references/OUTPUT_SCHEMA.md) <br>
- [ClawHub skill page](https://clawhub.ai/buksan1950/skills/reddit-readonly) <br>
- [Reddit public JSON endpoint](https://www.reddit.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [JSON command output and concise Markdown summaries with permalinks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only commands return standardized ok/data or ok/error objects; post and comment text is snippet-limited.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
