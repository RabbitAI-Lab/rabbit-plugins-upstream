## Description: <br>
Captures learnings, errors, and corrections to enable continuous improvement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent operators use this skill to record corrections, errors, feature requests, and recurring patterns into project memory so future agent work can use that context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Project memory files may capture sensitive conversation details, raw errors, tokens, personal data, or customer data. <br>
Mitigation: Review .learnings and promoted instruction files before committing or sharing them, and redact secrets and personal or customer data. <br>
Risk: Automatically promoted guidance can steer future agent behavior using stale or incorrect lessons. <br>
Mitigation: Prefer explicit prompts such as 'log this learning' and review promoted rules before adding them to CLAUDE.md, AGENTS.md, or Copilot instructions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/self-improving-agent) <br>
- [Publisher profile](https://clawhub.ai/user/thcjp) <br>
- [Agent Skills specification](https://agentskills.io/specification) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May create or update project memory files such as .learnings/LEARNINGS.md, .learnings/ERRORS.md, .learnings/FEATURE_REQUESTS.md, CLAUDE.md, AGENTS.md, and .github/copilot-instructions.md.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
