## Description: <br>
Lets agents operate GitHub through an OOMOL-connected account using the oo CLI for reading, creating, updating, and deleting GitHub data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to inspect and manage GitHub repositories, issues, pull requests, releases, workflows, files, collaborators, stars, and related account resources through an OOMOL-connected GitHub account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can perform write and destructive actions on GitHub resources connected to the user's account. <br>
Mitigation: Require explicit confirmation before repository deletion, file changes, workflow changes, collaborator changes, releases, public comments, or other state-changing actions. <br>
Risk: The skill operates through an OOMOL-connected GitHub account. <br>
Mitigation: Install only when OOMOL is intended to act on the user's GitHub account and review the GitHub connection scopes before use. <br>


## Reference(s): <br>
- [GitHub](https://github.com) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-github) <br>


## Skill Output: <br>
**Output Type(s):** [shell commands, JSON, guidance, configuration] <br>
**Output Format:** [Markdown with inline bash commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector responses are JSON objects with data and meta.executionId fields.] <br>

## Skill Version(s): <br>
1.0.4 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
