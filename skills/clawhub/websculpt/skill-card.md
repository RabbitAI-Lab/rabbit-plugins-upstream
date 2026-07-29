## Description: <br>
WebSculpt bootstraps a browser automation CLI and lifecycle skills for acquiring web information, scraping pages, calling APIs, and creating reusable command workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bqw1013](https://clawhub.ai/user/bqw1013) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to install or verify WebSculpt, then route browser automation, scraping, API-calling, command capture, repair, and library-management tasks to the appropriate lifecycle skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can install global npm packages and persistent agent skills. <br>
Mitigation: Probe the environment before installing, prefer project-local installation when possible, and confirm the npm package and version before global installs. <br>
Risk: Browser automation may use logged-in sessions or access content behind account walls. <br>
Mitigation: Use browser sessions intentionally, avoid exposing sensitive account data, and review retrieved information before relying on it. <br>
Risk: Exported command packages may contain sensitive evidence from prior automation runs. <br>
Mitigation: Review and redact exported command packages before sharing, migrating, or storing them outside the project. <br>


## Reference(s): <br>
- [WebSculpt ClawHub listing](https://clawhub.ai/bqw1013/skills/websculpt) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May install persistent lifecycle skills and route follow-on tasks to WebSculpt exploration, capture, maintenance, or library workflows.] <br>

## Skill Version(s): <br>
1.0.7 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
