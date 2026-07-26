## Description: <br>
Bookmark Intelligence Free helps users manually process recent X/Twitter bookmarks into local JSON knowledge cards using keyword-based summaries and tags. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to manually archive a small number of X/Twitter bookmarks, extract lightweight keyword summaries and tags, and store the results as local JSON for later review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The setup uses X/Twitter auth_token and ct0 cookies, which should be treated as sensitive account credentials. <br>
Mitigation: Keep the .env file private, restrict file permissions, do not commit or share it, and rotate or log out sessions if the values are exposed. <br>
Risk: The skill executes local setup and run commands and writes bookmark-derived data to local JSON files. <br>
Mitigation: Review commands before execution and inspect generated JSON files before sharing, syncing, or publishing local workspace contents. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/bookmark-intelligence-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, JSON files] <br>
**Output Format:** [Markdown guidance with inline shell commands and local JSON file outputs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Manual processing is limited to 10 bookmarks per month and writes results under life/resources/bookmarks/.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
