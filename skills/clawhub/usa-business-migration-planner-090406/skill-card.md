## Description: <br>
Helps users create repeatable plans, checklists, and decision support for selecting CDN providers other than Cloudflare when budget and timeout constraints matter. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to turn CDN vendor-selection questions into practical workflows, comparison checklists, and immediately usable decision support. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill name and automatic triggers may route unrelated business migration requests into a CDN vendor-selection workflow. <br>
Mitigation: Rename the skill to match its CDN-planning purpose, narrow the trigger keywords, and consider disabling implicit invocation before broad use. <br>
Risk: The skill can generate CDN planning guidance that may be stale or mismatched to current vendor limits, pricing, and timeout behavior. <br>
Mitigation: Review recommendations against current provider terms, pricing, timeout limits, and the user's stated traffic and budget constraints before acting on them. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Release](https://clawhub.ai/kyro-ma/skills/usa-business-migration-planner-090406) <br>
- [Source Demand Signal: V2EX CDN Provider Discussion](https://www.v2ex.com/t/1229340) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with plans, checklists, analysis, and optional code or command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should show assumptions, limits, validation notes, and remaining risks.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
