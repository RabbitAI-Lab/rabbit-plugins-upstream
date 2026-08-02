## Description: <br>
Fully automated multi-round code iteration with configurable N-dimension parallel review, onboarding/personalization, and a cross-assistant installer/update system with mandatory SHA256 checksum verification. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jingzhao-l](https://clawhub.ai/user/jingzhao-l) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineering teams use Iterate to run configurable multi-round code review and repair passes across a codebase, with automatic handling for small fixes and approval gates for architectural changes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: High-autonomy repository actions can edit files, run validation commands, commit, merge, and potentially push changes. <br>
Mitigation: Use only in repositories where that autonomy is intended; keep git.auto_merge and git.push_per_round disabled unless explicitly required. <br>
Risk: Security evidence notes conflicting documentation about automatic merge and push behavior. <br>
Mitigation: Review iterate.config.yaml before use and prefer pull requests or manual merges for protected branches. <br>
Risk: GitHub tokens passed on the command line can be exposed through shell history or process inspection. <br>
Mitigation: Avoid command-line tokens where possible and use safer credential handling for update flows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jingzhao-l/skills/iterate-skill) <br>
- [skills.sh listing](https://skills.sh/jingzhao-l/iterate-skill) <br>
- [Agent Skills standard](https://agentskills.io/) <br>
- [README](README.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON review output, shell commands, and generated configuration/files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May edit files, run validation commands, and perform git operations under user-configured safeguards.] <br>

## Skill Version(s): <br>
2.0.2 (source: frontmatter, pyproject.toml, ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
