## Description: <br>
Use the ClawdHub CLI to search, install, update, and publish agent skills from clawdhub.com. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jk50505k](https://clawhub.ai/user/jk50505k) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to run ClawdHub CLI workflows for searching, installing, updating, listing, and publishing agent skills. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill enables an agent to install, force-update, bulk-update, and publish ClawdHub skills. <br>
Mitigation: Require explicit approval before install, update, update --all, --force, --no-input, login, or publish commands. <br>
Risk: Publishing workflows can expose unchecked files or sensitive content from a local skill folder. <br>
Mitigation: Review the target publish directory before publishing and publish only folders checked for sensitive content. <br>
Risk: Unpinned installs or updates can change installed skill behavior unexpectedly. <br>
Mitigation: Prefer pinned versions and review the target registry and working directory before installation or update. <br>


## Reference(s): <br>
- [Clawdhub Copy skill page](https://clawhub.ai/jk50505k/skills/clawdhub-copy) <br>
- [ClawdHub registry](https://clawdhub.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes CLI command examples for install, authentication, search, update, list, and publish workflows.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
