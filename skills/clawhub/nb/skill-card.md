## Description: <br>
Manage notes, bookmarks, and notebooks using the nb CLI. Create, list, search, and organize notes across multiple notebooks with Git-backed versioning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bjesuiter](https://clawhub.ai/user/bjesuiter) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and note-taking users use this skill to get concise nb CLI guidance for creating, listing, searching, editing, deleting, syncing, and organizing Git-backed notes, bookmarks, todos, and notebooks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Manual changes inside ~/.nb notebooks can bypass nb indexing or expected Git commits. <br>
Mitigation: Prefer nb CLI commands for notebook changes and rebuild indexes only when needed. <br>
Risk: Sync, force delete, overwrite, and broad Git operations can affect private notes or notebook history. <br>
Mitigation: Review configured Git remotes and command targets before running nb sync, force delete, overwrite, or nb git operations. <br>


## Reference(s): <br>
- [nb GitHub repository](https://github.com/xwmx/nb) <br>
- [ClawHub skill page](https://clawhub.ai/bjesuiter/skills/nb) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the external nb CLI on macOS or Linux; no API keys were detected in the release evidence.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
