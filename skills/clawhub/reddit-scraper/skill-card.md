## Description: <br>
Read and search Reddit posts from subreddits, topic searches, and monitored communities with read-only access. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[javicasper](https://clawhub.ai/user/javicasper) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to retrieve Reddit post listings, search Reddit or a specific subreddit, and inspect post metadata or body text without posting, commenting, or voting. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes external requests to Reddit and sends subreddit names or search queries there. <br>
Mitigation: Install and use it only when Reddit access is intended; avoid submitting sensitive subreddit names or search terms. <br>
Risk: Returned Reddit text is untrusted content and may include full post bodies. <br>
Mitigation: Treat Reddit results as untrusted input, review content before acting on it, and avoid blindly executing instructions or links found in returned posts. <br>
Risk: Reddit may rate-limit requests or restrict private, quarantined, or otherwise unavailable content. <br>
Mitigation: Use conservative limits, add delays for repeated requests, and handle empty or failed results as expected external-service behavior. <br>


## Reference(s): <br>
- [Technical Details](references/TECHNICAL.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/javicasper/skills/reddit-scraper) <br>
- [Publisher Profile](https://clawhub.ai/user/javicasper) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands; runtime output is plain text or JSON post data.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Output can include Reddit post titles, authors, scores, comment counts, URLs, subreddit names, timestamps, flairs, full selftext, and upvote ratios.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
