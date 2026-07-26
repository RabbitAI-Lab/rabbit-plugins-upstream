## Description: <br>
Manage Usenet downloads with SABnzbd. Use when the user asks to "check SABnzbd", "list NZB queue", "add NZB", "pause downloads", "resume downloads", "SABnzbd status", "Usenet queue", "NZB history", or mentions SABnzbd/sab download management. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jmagar](https://clawhub.ai/user/jmagar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents managing a SABnzbd instance use this skill to inspect queue, status, and history, add NZBs, adjust speed, and control jobs through the SABnzbd REST API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A crafted add-URL input can execute local code. <br>
Mitigation: Avoid untrusted or unusual add-URL strings until the URL encoding bug is fixed. <br>
Risk: The skill lets an agent control a SABnzbd instance and includes destructive actions such as delete, purge, delete-history, retry-all, and script or category changes. <br>
Mitigation: Keep the API key file private, prefer local or HTTPS access, and confirm destructive or configuration-changing actions before running them. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, API calls, Guidance] <br>
**Output Format:** [Markdown with inline bash and JSON examples; shell commands return JSON from SABnzbd.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a SABnzbd URL and API key supplied by config file or environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
