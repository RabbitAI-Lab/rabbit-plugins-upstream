## Description: <br>
Helps agents document architecture decisions, rationale-focused comments, README updates, changelogs, and API documentation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to create ADRs, improve project documentation, maintain API docs, and preserve the rationale behind technical decisions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate on broad documentation requests and produce changes beyond the user's intended scope. <br>
Mitigation: Review proposed documentation changes for scope, accuracy, and relevance before accepting them. <br>
Risk: Generated ADRs, README updates, changelogs, or API docs may misstate design rationale or project behavior. <br>
Mitigation: Have project maintainers verify technical claims and decision rationale before publication. <br>
Risk: The skill may propose git commits after documentation work. <br>
Mitigation: Inspect diffs and commit messages before running or approving any git command. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/paudyyin/skills/documentation-and-adrs) <br>
- [Publisher profile](https://clawhub.ai/user/paudyyin) <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown prose, ADR templates, documentation checklists, code comments, and proposed shell or git commands when relevant] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose documentation edits or git commits; users should review generated documentation and commits before accepting them.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
