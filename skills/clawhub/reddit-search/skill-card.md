## Description: <br>
Search Reddit for subreddits and get information about them. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thesethrose](https://clawhub.ai/user/thesethrose) <br>

### License/Terms of Use: <br>
ISC <br>


## Use Case: <br>
Developers and agents use this skill to look up subreddit details, discover communities by query or listing, and inspect hot posts from a named subreddit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Subreddit names and search terms are sent to reddit.com. <br>
Mitigation: Avoid using secrets, internal project names, or sensitive identifiers as queries. <br>
Risk: Dependency review may be needed when installing or updating the HTTP client dependency. <br>
Mitigation: Install with the provided lockfile or review and pin axios before deployment. <br>
Risk: Reddit rate limits or availability issues can interrupt lookups. <br>
Mitigation: Retry later on rate-limit errors and verify important results against Reddit directly. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thesethrose/skills/reddit-search) <br>
- [Reddit website JSON endpoints](https://www.reddit.com) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text CLI output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results depend on Reddit availability, rate limits, and public subreddit data.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
