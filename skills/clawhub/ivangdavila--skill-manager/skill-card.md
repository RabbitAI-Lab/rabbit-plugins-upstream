## Description: <br>
Manage installed skills lifecycle: suggest by context, track installations, check updates, and cleanup unused. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use Skill Manager to identify context-relevant skills, manage install, update, and removal workflows, and maintain a concise local inventory of accepted and declined skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Skill installation and update commands can download and execute code from the ClawHub registry. <br>
Mitigation: Review each skill before approving installation or update, and require explicit user consent before running npx clawhub install, update, or uninstall commands. <br>
Risk: The local inventory records installed skills and user-stated decline reasons in ~/skill-manager/inventory.md. <br>
Mitigation: Keep decline reasons brief and avoid sensitive information; use the inventory only for skill lifecycle tracking. <br>


## Reference(s): <br>
- [Skill Manager on ClawHub](https://clawhub.ai/ivangdavila/skill-manager) <br>
- [Skill Lifecycle Management](lifecycle.md) <br>
- [Context-Based Skill Suggestions](suggestions.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires explicit user approval before install, update, or removal actions; inventory entries are stored locally in ~/skill-manager/inventory.md.] <br>

## Skill Version(s): <br>
1.0.3 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
