## Description: <br>
Browse and search Reddit in read-only mode using public JSON endpoints. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tristanmanchester](https://clawhub.ai/user/tristanmanchester) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agents use this skill to browse public Reddit posts and comments, search topics across subreddits, inspect threads, and prepare shortlists of permalinks for manual review or reply drafting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-directed subreddit names, post URLs or IDs, and search terms are sent to reddit.com. <br>
Mitigation: Install only when this network behavior is acceptable; scope searches narrowly and avoid entering sensitive terms. <br>
Risk: Reddit may rate limit requests or return HTML instead of JSON, causing partial or failed results. <br>
Mitigation: Use small limits first and slower pacing through REDDIT_RO_MIN_DELAY_MS, REDDIT_RO_MAX_DELAY_MS, and REDDIT_RO_TIMEOUT_MS when requests fail. <br>
Risk: Read-only results can be incomplete because continuation comments are not fetched and text snippets may be truncated. <br>
Mitigation: Treat shortlists as discovery aids and open the provided permalinks for final review before replying manually. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tristanmanchester/skills/reddit-read-only) <br>
- [Publisher profile](https://clawhub.ai/user/tristanmanchester) <br>
- [Output schema](references/OUTPUT_SCHEMA.md) <br>
- [Reddit public endpoint](https://www.reddit.com) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Markdown, Shell commands, Guidance] <br>
**Output Format:** [JSON command output and concise Markdown summaries with Reddit permalinks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands return ok/data or ok/error JSON; post and comment snippets may be truncated and thread results may be partial.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
