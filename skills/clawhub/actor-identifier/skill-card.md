## Description: <br>
Actor Identifier helps teams analyze Git repository collaboration patterns across one or more repositories, generate aggregate reports, define custom metrics, and prepare CI/CD reporting workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, engineering managers, and platform teams use this skill to analyze repository-level collaboration health, compare multiple repositories, configure custom metrics, and generate recurring team workflow reports. The artifact states that reports are intended for team process improvement, not individual evaluation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security summary says the CI examples can modify repositories and notify Slack while the artifact also describes a no-write, no-network safety contract. <br>
Mitigation: Review the skill before automated or private-repository use; disable report commits, repository pushes, and Slack notifications unless those actions and credentials are explicitly approved. <br>
Risk: Custom metric query strings can cause unsafe command execution if treated as arbitrary shell commands. <br>
Mitigation: Execute only validated, read-only Git commands from a real allowlist and reject custom queries that access network, secrets, parent directories, or non-repository paths. <br>
Risk: Scheduled CI runs and generated reports can expose repository activity patterns or use broad push tokens. <br>
Mitigation: Scope tokens narrowly, keep generated reports in approved locations, redact secrets before display, and limit analysis to user-provided repositories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/actor-identifier) <br>
- [SkillHub homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell snippets, CI/configuration examples, and JSON-shaped analysis results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May describe Markdown, HTML, or PDF repository reports; examples focus on repository-level aggregate metrics and workflow improvement guidance.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
