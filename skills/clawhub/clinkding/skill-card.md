## Description: <br>
Manage linkding bookmarks: save URLs, search, tag, organize, and retrieve a personal bookmark collection. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[daveonkels](https://clawhub.ai/user/daveonkels) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to manage a Linkding bookmark collection from an agent-assisted terminal workflow: saving URLs, searching bookmarks, tagging items, organizing bundles, and retrieving reading lists. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Linkding API token, and exposing the token can grant access to a user's bookmark data. <br>
Mitigation: Keep the API token private, prefer protected config files or environment variables, and avoid passing tokens in command lines that may be logged. <br>
Risk: Delete, archive, upload, and download actions can change or expose bookmark data and attached files. <br>
Mitigation: Review destructive or file-transfer commands before approving them, especially when operating on bookmark or asset IDs. <br>
Risk: Automatic URL summarization may send private, internal, or token-bearing URLs to another tool or service. <br>
Mitigation: Avoid automatic summarization for internal, private, or token-bearing URLs unless the user explicitly approves the handling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/daveonkels/skills/clinkding) <br>
- [clinkding GitHub repository](https://github.com/daveonkels/clinkding) <br>
- [linkding project](https://github.com/sissbruecker/linkding) <br>
- [clinkding releases](https://github.com/daveonkels/clinkding/releases) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance, Text, JSON] <br>
**Output Format:** [Markdown guidance with inline shell commands and CLI output options] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can guide use of human-readable tables, JSON, or plain text output from the clinkding CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
