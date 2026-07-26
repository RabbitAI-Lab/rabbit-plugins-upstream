## Description: <br>
Initializes workspace-level AGENTS.md constraints that make an AI agent ask before changing files, deleting files, or altering its core operating rules. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sinanxrasheed](https://clawhub.ai/user/sinanxrasheed) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to add explicit operating constraints to AGENTS.md so future file changes, deletions, and rule updates require discussion or authorization. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing the constraints may cause future agents to refuse or slow down file-changing requests until the user discusses or authorizes them. <br>
Mitigation: Review the operating constraints before activation and use the documented rollback path by removing the Core Constraints section from AGENTS.md if the behavior is no longer wanted. <br>
Risk: Authorization key values could be exposed if a user or agent records the raw keys in workspace files. <br>
Mitigation: Record only verification state such as VERIFIED or ACTIVE, and never write real authorization key values into files. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sinanxrasheed/skills/constitutional-setup) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown instructions and AGENTS.md configuration text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts the user for authorization-key verification state and instructs the agent not to record raw key values.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
