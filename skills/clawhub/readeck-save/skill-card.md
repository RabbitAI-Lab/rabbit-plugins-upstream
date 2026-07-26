## Description: <br>
Save articles to Readeck (self-hosted read-it-later app). Use when the user wants to save an article for later reading, add something to their reading list, or send a page to Readeck. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nickian](https://clawhub.ai/user/nickian) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to save a URL into a configured self-hosted Readeck read-it-later instance for later reading. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A configured Readeck server will receive and fetch user-provided URLs, which may expose private, internal, or token-bearing links. <br>
Mitigation: Save only URLs intended for that Readeck instance, and avoid private, internal, or token-bearing URLs unless storage and fetching by that server is intended. <br>
Risk: A compromised or incorrect Readeck endpoint could receive the configured API token and saved URLs. <br>
Mitigation: Install this only for a trusted Readeck instance, check READECK_URL carefully, and use a revocable or least-privileged API token when supported. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, configuration, text] <br>
**Output Format:** [Markdown guidance with shell commands and plain-text command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires READECK_URL and READECK_API_TOKEN environment variables.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
