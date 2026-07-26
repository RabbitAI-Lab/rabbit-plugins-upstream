## Description: <br>
Complete memory system combining LanceDB auto-recall, Git-Notes structured memory, and file-based workspace search. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ktpriyatham](https://clawhub.ai/user/ktpriyatham) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to configure persistent memory across conversation recall, structured decision logging, and workspace file search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill silently and automatically stores user and workspace context, which can reduce user visibility into what is retained. <br>
Mitigation: Remove or override silent-operation instructions and require reviewable memory actions before deployment. <br>
Risk: Automatic capture and auto-flush can retain sensitive work unless scope and exclusion rules are defined. <br>
Mitigation: Disable auto-capture or auto-flush for sensitive work, define excluded paths and data categories, and confirm stored memories can be reviewed and deleted. <br>
Risk: Conversation memory may send content to the configured embedding provider. <br>
Mitigation: Confirm what data is sent to the embedding provider and configure the provider only for approved data categories. <br>


## Reference(s): <br>
- [Triple Memory Skill Page](https://clawhub.ai/ktpriyatham/skills/triple-memory-skill) <br>
- [Triple Memory Setup Reference](references/SETUP.md) <br>
- [Auto-Flush Configuration](references/auto-flush-config.json) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown with JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes setup instructions for memory plugins, Git-Notes memory commands, file-search usage, and auto-flush configuration.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
