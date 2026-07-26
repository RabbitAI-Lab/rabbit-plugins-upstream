## Description: <br>
Helps AI-agent users, skill authors, maintainers, and teams create practical workflows, checklists, analyses, or implementation support for Agent Browser-style productivity work. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kyro-ma](https://clawhub.ai/user/kyro-ma) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI-agent users, skill authors, maintainers, and teams use this skill to turn Agent Browser-style productivity requests into practical plans, artifacts, reusable checklists, analyses, code changes, or decision support. It emphasizes clear assumptions, local-hardware-friendly approaches, and a short verification note. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The activation wording is broad and may cause the skill to be invoked during unrelated browser, automation, CLI, or bug-fix tasks. <br>
Mitigation: Prefer explicit invocation by skill name and confirm that the request matches Agent Browser-style productivity workflow support before relying on the output. <br>
Risk: The skill produces guidance, plans, code changes, shell commands, or configuration suggestions that could be incorrect for a user's environment. <br>
Mitigation: Review proposed artifacts before use, test code or commands in a safe local environment, and keep assumptions and validation notes visible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/work-productivity-agent-browser-workflow-helper-200354) <br>
- [Requirement Plan](artifact/references/requirement-plan.md) <br>
- [Agent Browser demand signal](https://clawhub.ai/skills/agent-browser-clawdbot) <br>
- [Evaluate removing Playwright as a first-class browser mode](https://github.com/manishiitg/coding-agent-loop/issues/128) <br>
- [SVIEW local-hardware workflow signal](https://news.ycombinator.com/item?id=48892881) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with optional code, shell command, checklist, or configuration blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Tailored to the user's stated outcome and includes assumptions, limits, validation notes, and follow-up work when relevant.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
