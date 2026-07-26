## Description: <br>
Create and manage blog posts on Bear Blog with extended Markdown, custom post attributes, and browser-based publishing workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[azade-c](https://clawhub.ai/user/azade-c) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and content operators use this skill to help an agent draft, format, publish, edit, list, unpublish, or delete Bear Blog posts through an authenticated browser session. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: An authenticated browser session can publish, unpublish, or delete live Bear Blog content, including examples that bypass a delete confirmation dialog. <br>
Mitigation: Require explicit user confirmation before publish, unpublish, or delete actions, and verify the exact blog subdomain plus post title or URL before execution. <br>
Risk: Login workflows may expose Bear Blog credentials if passwords are typed into ordinary chat or saved logs. <br>
Mitigation: Use protected secret handling where available and avoid placing passwords in normal chat transcripts, examples, or persistent logs. <br>


## Reference(s): <br>
- [Bear Blog](https://bearblog.dev) <br>
- [ClawHub Skill Page](https://clawhub.ai/azade-c/skills/bearblog) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance with browser action examples and post templates] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires an authenticated Bear Blog browser session and browser-enabled agent configuration.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
