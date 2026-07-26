## Description: <br>
Scrapes posts from a Facebook group and returns structured post metadata including IDs, permalinks, authors, timestamps, body text, media, reactions, comments, shares, and diagnostics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to export post data from Facebook groups they can access in an authenticated browser session. It is suited for collecting group feed metadata, monitoring group activity, and preparing structured JSON records for downstream analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses a logged-in Facebook session to collect group post data, which can include sensitive personal or community information. <br>
Mitigation: Install and run it only for groups and data you are allowed to access, review Facebook's rules and group privacy expectations, and avoid collecting data from private or membership-only groups without appropriate permission. <br>
Risk: Large requested post counts can cause unintended bulk collection. <br>
Mitigation: Keep requested counts small unless bulk export is intentional, and require explicit user confirmation before collecting more than 50 posts. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/browseract-cli/skills/facebook-groups-scrape-posts) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Shell commands, Guidance] <br>
**Output Format:** [JSON output with Markdown instructions and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Structured post records include post, group, author, media, reaction, comment, share, and pagination diagnostic fields.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
