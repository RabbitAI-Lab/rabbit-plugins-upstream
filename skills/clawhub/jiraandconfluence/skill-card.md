## Description: <br>
CLI tool for interacting with Atlassian Jira and Confluence. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[festoinc](https://clawhub.ai/user/festoinc) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to manage Jira issues, projects, users, and Confluence pages from the command line. It supports read operations and write operations such as issue creation, updates, comments, workflow transitions, assignment changes, and Confluence edits. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make real changes in Jira and Confluence using the configured Atlassian token. <br>
Mitigation: Use a least-privilege Atlassian API token, keep the .env file private, start with tightly scoped YAML settings, and review commands before allowing issue creation, updates, comments, assignment changes, workflow transitions, or Confluence edits. <br>
Risk: The skill depends on an external npm package controlled by the third-party publisher. <br>
Mitigation: Install only if the publisher and package are trusted, and prefer pinning or reviewing the package before use. <br>


## Reference(s): <br>
- [Jira-AI GitHub Repository](https://github.com/festoinc/jira-ai) <br>
- [ClawHub Skill Page](https://clawhub.ai/festoinc/skills/jiraandconfluence) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and configuration examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Jira JQL, YAML settings, and environment variable examples for Atlassian authentication.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
