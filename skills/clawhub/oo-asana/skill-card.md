## Description: <br>
Asana connector for reading, creating, updating, and deleting Asana workspace data through an OOMOL-connected account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and workspace operators use this skill to let an agent retrieve and manage Asana workspaces, projects, tasks, users, teams, tags, stories, attachments, and custom fields. It supports read workflows as well as confirmed write and destructive changes to Asana objects. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change or delete Asana data, including tasks, projects, tags, comments, attachments, membership, dependencies, and workspace or project settings. <br>
Mitigation: Review the exact payload, target object, and expected effect before approving write or destructive actions. <br>
Risk: Use depends on the oo CLI and OOMOL connection model for access to the user's Asana workspace. <br>
Mitigation: Install only when the publisher and connection model are trusted for the workspace being accessed. <br>


## Reference(s): <br>
- [ClawHub Asana Skill](https://clawhub.ai/oomol/skills/oo-asana) <br>
- [Asana Homepage](https://asana.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return Asana connector JSON responses that include data and execution metadata.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
