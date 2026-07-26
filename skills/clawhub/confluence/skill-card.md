## Description: <br>
Search and manage Confluence pages and spaces using confluence-cli. Read documentation, create pages, and navigate spaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[francisbrero](https://clawhub.ai/user/francisbrero) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and teams with Confluence access use this skill to search, read, list, create, update, and export Confluence pages and spaces through confluence-cli. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill relies on confluence-cli and an Atlassian API token, which can grant access to Confluence content. <br>
Mitigation: Install confluence-cli only if it is trusted, treat the API token and ~/.confluence-cli/config.json as sensitive, and avoid exposing them in logs or screenshots. <br>
Risk: Create and update commands can change Confluence pages or spaces. <br>
Mitigation: Confirm the target space, page ID, parent page, and content before running write operations. <br>


## Reference(s): <br>
- [Confluence skill on ClawHub](https://clawhub.ai/francisbrero/skills/confluence) <br>
- [confluence-cli GitHub repository](https://github.com/pchuri/confluence-cli) <br>
- [Atlassian API token management](https://id.atlassian.com/manage-profile/security/api-tokens) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires confluence-cli and a Confluence API token configured outside the agent.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
