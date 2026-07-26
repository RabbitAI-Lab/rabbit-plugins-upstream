## Description: <br>
Use the ClawdHub CLI to search, install, update, and publish agent skills from clawdhub.com. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[steipete](https://clawhub.ai/user/steipete) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill when they need an agent to run ClawdHub CLI workflows for discovering skills, installing or updating local skills, authenticating, listing installs, or publishing skill folders. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill exposes broad CLI actions for global npm installation, login, publishing, forced updates, and non-interactive updates. <br>
Mitigation: Require explicit approval before running global npm install, login, publish, update --all, --force, or --no-input commands. <br>
Risk: CLI actions can modify local skill directories or publish unintended files. <br>
Mitigation: Verify the registry URL, target directory, package provenance, and files being published before execution. <br>


## Reference(s): <br>
- [Clawdhub skill page](https://clawhub.ai/steipete/skills/clawdhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and configuration notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands may install, update, authenticate, or publish skills through the ClawdHub CLI.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
