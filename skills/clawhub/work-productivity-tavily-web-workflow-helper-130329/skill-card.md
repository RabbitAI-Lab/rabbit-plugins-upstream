## Description: <br>
Helps agent users and skill authors create, validate, and improve Tavily-style web productivity workflows, including bug fixing, safety hardening, reliability improvements, and adjacent workflow design. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to turn Tavily-style web and search workflow needs into practical plans, templates, checklists, code changes, or decision support. It is intended for improving setup safety, reliability, and repeatable productivity workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation wording may route general web, search, or productivity requests into this helper. <br>
Mitigation: Use explicit invocation or narrow triggers when clean routing is important. <br>
Risk: Workflow and implementation guidance may be incomplete for a user's specific environment. <br>
Mitigation: Review generated plans, code changes, and checklists against local requirements before deployment. <br>


## Reference(s): <br>
- [Requirement Plan](references/requirement-plan.md) <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-tavily-web-workflow-helper-130329) <br>
- [Tavily search demand signal](https://clawhub.ai/skills/openclaw-tavily-search) <br>
- [Web research capability issue](https://github.com/hugimuni-labs/brnrd/issues/411) <br>
- [Multi Search Engine demand signal](https://clawhub.ai/skills/multi-search-engine) <br>
- [Agent Browser demand signal](https://clawhub.ai/skills/agent-browser-clawdbot) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code, shell command, checklist, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include assumptions, validation notes, and remaining risks when helpful.] <br>

## Skill Version(s): <br>
0.20260729.110214 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
