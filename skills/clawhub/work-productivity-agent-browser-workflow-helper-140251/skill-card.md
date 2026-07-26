## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create practical Agent Browser-style workflows for debugging, reliability hardening, safety review, and adjacent skill development. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to turn Agent Browser-style workflow needs into actionable plans, checklists, code changes, workflow artifacts, or decision support. It is intended for practical browser automation, debugging, reliability, and safety-oriented workflow help. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation terms may cause the skill to run for general browser, automation, CLI, or bug-fix requests where Agent Browser-specific help was not intended. <br>
Mitigation: Use the skill when Agent Browser workflow support is specifically desired, and narrow triggers in a future revision. <br>
Risk: The skill can produce workflow, checklist, code, shell command, or configuration guidance that may be incomplete or incorrect for a user's environment. <br>
Mitigation: Review generated outputs before use, validate them against the stated success criteria, and scan or test code and commands before deployment. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/kyro-ma/skills/work-productivity-agent-browser-workflow-helper-140251) <br>
- [Agent Browser demand signal](https://clawhub.ai/skills/agent-browser-clawdbot) <br>
- [Playwright browser mode discussion](https://github.com/manishiitg/mcp-agent-builder-go/issues/128) <br>
- [Heredoc-style agent workflow discussion](https://www.v2ex.com/t/1227024) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code, shell command, checklist, and configuration blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs should expose assumptions, validation notes, remaining risks, and practical next steps when useful.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
