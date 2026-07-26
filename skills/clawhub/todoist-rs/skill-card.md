## Description: <br>
Manage Todoist tasks when the user mentions Todoist, task lists, adding tasks, completing tasks, or interacting with their Todoist account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[luoandorder](https://clawhub.ai/user/luoandorder) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to let an agent list, add, update, complete, reopen, and delete Todoist tasks through the configured td CLI. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can change live Todoist tasks through add, edit, complete, bulk complete, and delete actions. <br>
Mitigation: Invoke it explicitly for Todoist work and review task-changing commands before execution. <br>
Risk: Read commands can use cached Todoist data. <br>
Mitigation: Use td sync or command sync flags when fresh task state is needed before making decisions. <br>
Risk: Installation depends on a third-party Homebrew tap or Cargo package. <br>
Mitigation: Verify the Homebrew tap or Cargo package source before installation. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/luoandorder/skills/todoist-rs) <br>
- [Project Homepage](https://github.com/LuoAndOrder/todoist-rs) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires the td CLI and a configured Todoist account.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
