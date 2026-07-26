## Description: <br>
Three Minds runs three Claude Code agents with different personas in a shared workspace so they can review, modify, test, and iterate on a task until they reach consensus. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[enderfga](https://clawhub.ai/user/enderfga) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and engineers use this skill to coordinate multi-perspective coding work such as code review, refactoring, feature development, bug fixing, documentation improvement, research brainstorming, and paper review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Spawned coding agents can read and modify the selected workspace and run commands without normal permission prompts. <br>
Mitigation: Use the skill in a clean branch or disposable checkout, avoid workspaces with secrets in files or environment variables, and review resulting changes before keeping them. <br>
Risk: The skill saves transcripts that may include task details, agent outputs, or excerpts from project files. <br>
Mitigation: Review generated transcripts before sharing or committing them, and delete transcripts that contain sensitive information. <br>


## Reference(s): <br>
- [ClawHub listing](https://clawhub.ai/enderfga/skills/three-minds) <br>
- [README](artifact/README.md) <br>
- [Skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Code, Shell commands, Guidance] <br>
**Output Format:** [Terminal text, Markdown transcript, optional JSON session data, and workspace file changes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs up to a configured maximum number of collaboration rounds and saves a timestamped Markdown transcript in the selected workspace.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata; artifact frontmatter and package.json report 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
