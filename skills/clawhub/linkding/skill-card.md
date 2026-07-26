## Description: <br>
Manage bookmarks with Linkding through its REST API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jmagar](https://clawhub.ai/user/jmagar) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to search, create, update, archive, delete, tag, and bundle bookmarks in a configured Linkding instance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses the user's configured Linkding API key to read and change bookmark data. <br>
Mitigation: Install only when the agent should be allowed to access that Linkding account, and store the API token in the documented credentials file or environment variable. <br>
Risk: Delete operations can remove bookmarks or bundles from Linkding. <br>
Mitigation: Require explicit user confirmation before running destructive bookmark or bundle commands. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jmagar/skills/linkding) <br>
- [README.md](artifact/README.md) <br>
- [SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a configured Linkding URL and API token; API responses are JSON.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
