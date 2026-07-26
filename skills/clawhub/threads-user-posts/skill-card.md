## Description: <br>
Fetches public posts from a Threads user profile, including post text, engagement metrics, media details, and pagination state from page data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agent operators use this skill to collect posts from public or otherwise authorized Threads profiles in a browser session for review, monitoring, or data export. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Browser automation and network-response reading can expose session context or credentials if handled carelessly. <br>
Mitigation: Use an intended browser session, do not capture credentials, and review any batch script before running it. <br>
Risk: Collecting Threads profile posts at scale or from unauthorized profiles can violate platform rules or user privacy expectations. <br>
Mitigation: Use the skill only on public or otherwise authorized profiles and avoid large-scale or parallel scraping. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/browseract-cli/skills/threads-user-posts) <br>
- [Threads](https://www.threads.com) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Code, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON extraction output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a browser-act browser session and reads Threads profile page data visible to the user.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
