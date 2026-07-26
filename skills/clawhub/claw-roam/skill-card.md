## Description: <br>
Sync OpenClaw workspace between multiple machines via Git for workspace backup, migration, status checks, and multi-device continuity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[reed1898](https://clawhub.ai/user/reed1898) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and OpenClaw users use this skill to keep an OpenClaw workspace synchronized across machines through a Git remote. It helps commit, push, pull, merge, and inspect workspace sync state before switching devices or backing up a workspace. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The sync workflow can upload private OpenClaw memory, logs, context, and skills to the user's configured Git remote. <br>
Mitigation: Use a private trusted repository, add .gitignore rules for secrets and local-only files, run git status before pushing, and avoid automatic cron pushes unless continuous upload is intentional. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and a Bash helper script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Commands operate on the user's OpenClaw workspace and configured Git remote.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
