## Description: <br>
This skill supports AllTrails hiking and trail queries, including trail search, trail details, reviews, photos, conditions, saved trails, completed trails, and user activity. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[chrischall](https://clawhub.ai/user/chrischall) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to answer hiking and trail questions with AllTrails data, including trail discovery, route details, reviews, photos, weather, saved lists, completed trails, and account activity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The integration is unofficial and reverse-engineered, and AllTrails API behavior or access controls may change. <br>
Mitigation: Use it for personal AllTrails tasks, expect possible breakage, and run diagnostics when requests fail. <br>
Risk: Requests route through a signed-in AllTrails browser tab and can read personal AllTrails account data. <br>
Mitigation: Install only when read access through the signed-in browser session is acceptable, and constrain skill use where the agent supports it. <br>
Risk: Broad hiking or trail prompts may trigger the skill and access AllTrails data through the active session. <br>
Mitigation: Avoid bulk extraction and review agent permissions or invocation controls before use. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/chrischall/skills/alltrails) <br>
- [npm package](https://www.npmjs.com/package/alltrails-mcp) <br>
- [Publisher profile](https://clawhub.ai/user/chrischall) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline JSON and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include compact trail summaries, account-derived read-only data, GPX route output, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
2.1.1 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
