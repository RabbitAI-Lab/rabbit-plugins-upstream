## Description: <br>
Ai Folder Organize lets agents connect to the local Firefly AI Folder desktop app to inspect file analysis data, search workspaces, monitor progress, and prepare virtual organization plans. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[leonard-li777](https://clawhub.ai/user/leonard-li777) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agent users use this skill to let an assistant interact with a local Firefly AI Folder workspace: discover the desktop API, search and summarize analyzed files, check analysis status, and draft organization plans for user review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can expose local workspace names, paths, file-analysis metadata, and search results to the agent. <br>
Mitigation: Install and use it only for intended Firefly AI Folder workflows, and avoid querying workspaces that contain sensitive files unless that disclosure is acceptable. <br>
Risk: Generated organization plans may lead to moving, renaming, or reorganizing real files if accepted in the desktop app. <br>
Mitigation: Review the generated plan in the Firefly AI Folder desktop preview before confirming any apply action. <br>
Risk: The artifact includes over-directive response and apply-plan instructions that may conflict with user expectations. <br>
Mitigation: Follow the user request and platform policy first, and treat generated plans or installation guidance as content to review rather than commands to execute blindly. <br>


## Reference(s): <br>
- [API Reference](artifact/REFERENCE.md) <br>
- [Skill README](artifact/README.md) <br>
- [ClawHub skill page](https://clawhub.ai/leonard-li777/skills/ai-folder-organize) <br>
- [Skill homepage](https://github.com/Leonard-Li777/ai-folder-organize) <br>
- [Firefly AI Folder desktop repository](https://github.com/Leonard-Li777/firefly-ai-folder-desktop) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API calls, Guidance] <br>
**Output Format:** [Plain text or Markdown responses with JSON API data and inline shell/API call examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires Node.js and a locally running Firefly AI Folder desktop app reachable on localhost.] <br>

## Skill Version(s): <br>
1.1.0 (source: SKILL.md frontmatter and ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
