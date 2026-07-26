## Description: <br>
Triple Memory combines LanceDB auto-recall, Git-Notes structured memory, and file-based workspace search to help agents retain and reuse context across sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ktpriyatham](https://clawhub.ai/user/ktpriyatham) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent operators use this skill to configure persistent memory across conversation recall, structured decision storage, and workspace file search. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Automatic persistent memory can store and reuse sensitive user or project context across sessions. <br>
Mitigation: Enable auto-capture only where persistent memory is intended, scope it narrowly for sensitive work, and confirm stored memories can be inspected, edited, and deleted. <br>
Risk: Silent memory operation can make retention of user context unclear to affected users. <br>
Mitigation: Make memory use visible in the deployment environment and align capture behavior with user consent and organizational policy. <br>
Risk: Embedding configuration requires API-key handling and may expose secrets if copied into committed files. <br>
Mitigation: Keep API keys in environment variables or secret storage, and review configuration files before committing or sharing them. <br>


## Reference(s): <br>
- [Triple Memory Setup Reference](references/SETUP.md) <br>
- [ClawHub skill page](https://clawhub.ai/ktpriyatham/skills/triple-memory) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown with JSON and bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes setup snippets, workspace memory templates, and file-search script guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
