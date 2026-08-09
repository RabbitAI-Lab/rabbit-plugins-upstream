## Description: <br>
Detect and preserve human code edits. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tobiaswestholm](https://clawhub.ai/user/tobiaswestholm) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill when they need to preserve human edits before modifying files and commit completed edit series to Git. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may persist repository changes through local Git commits. <br>
Mitigation: Review staged changes and confirm commits are limited to files involved in the requested task before relying on it in sensitive repositories. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/tobiaswestholm/skills/respect-human-edits) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands] <br>
**Output Format:** [Markdown with inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Prompts the agent to inspect Git ignore and diff state before editing and to create concise commits after edit series.] <br>

## Skill Version(s): <br>
1.0.1 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
