## Description: <br>
Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jingzhao-l](https://clawhub.ai/user/jingzhao-l) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use Iterate to run multi-round code quality, security, performance, architecture, and test-focused review cycles over a project, with direct fixes for small issues and approval gates for larger architectural changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can edit code, run configured validation commands, create git commits, and install a helper CLI. <br>
Mitigation: Use it only in repositories where that level of automation is acceptable, and prefer a clean branch or worktree before starting a run. <br>
Risk: Automatic merge or push behavior can publish or integrate changes before they receive human review if enabled. <br>
Mitigation: Keep merge and push disabled unless explicitly desired, and review generated changes before integrating them. <br>
Risk: Validation commands are executable project configuration and may affect the local environment. <br>
Mitigation: Review validation.commands and the command whitelist before use, and keep only trusted lint, test, build, or audit commands configured. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/jingzhao-l/skills/iterate-skill) <br>
- [README.md](README.md) <br>
- [SKILL.md](SKILL.md) <br>
- [Default Configuration](config/iterate.config.yaml) <br>
- [npm Installer Package](https://www.npmjs.com/package/iterate-skill-installer) <br>
- [Agent Skills Standard](https://agentskills.io/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands, code changes, and configuration files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update project files, generated project context, configuration, validation results, commits, and local branch or worktree state depending on user configuration.] <br>

## Skill Version(s): <br>
2.3.0 (source: frontmatter, pyproject.toml, npm-installer/package.json, changelog) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
