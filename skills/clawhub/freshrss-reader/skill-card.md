## Description: <br>
Query headlines and articles from a self-hosted FreshRSS instance with category, time range, unread, and count filters. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickian](https://clawhub.ai/user/nickian) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to fetch recent headlines, unread items, feeds, and categories from their own FreshRSS reader through the Google Reader compatible API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires access to the user's FreshRSS account and API password. <br>
Mitigation: Install only from a trusted publisher, use an HTTPS FreshRSS URL, prefer a dedicated API password, and revoke that password when the skill is no longer needed. <br>
Risk: The skill runs authenticated requests against the configured FreshRSS server. <br>
Mitigation: Review the skill before deployment and confirm that the configured server URL and credentials are intended for this use. <br>


## Reference(s): <br>
- [FreshRSS Reader on ClawHub](https://clawhub.ai/nickian/skills/freshrss-reader) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell command examples and plain text headline output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Headlines include published date, source, article URL, and categories when returned by FreshRSS.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
