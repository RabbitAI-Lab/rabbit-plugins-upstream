## Description: <br>
Interact with Obsidian vaults through the Obsidian CLI to read, create, search, and manage notes, tasks, and properties, with additional commands for plugin and theme development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[psprosen-dev](https://clawhub.ai/user/psprosen-dev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, note-takers, and knowledge workers use this skill to operate an open Obsidian vault from an agent-assisted command-line workflow. It supports note lookup and maintenance, vault search, task and property updates, and plugin or theme debugging. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Commands can modify notes, reload plugins, take screenshots, inspect the DOM, or run JavaScript in Obsidian. <br>
Mitigation: Prefer read-only commands for ordinary note lookups and require explicit review before write, plugin reload, screenshot, DOM inspection, or JavaScript execution commands. <br>


## Reference(s): <br>
- [Obsidian CLI documentation](https://help.obsidian.md/cli) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Obsidian to be open and an Obsidian CLI command target to be available.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
