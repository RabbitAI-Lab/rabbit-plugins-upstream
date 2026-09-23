## Description: <br>
bsession helps agents set up browser automation sessions, perform one-shot website information fetches, and create persistent browser sessions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation users can use this skill to drive browser sessions for navigation, page interaction, content extraction, screenshots, login workflows, and repeated web tasks. It is not suited to complex decisions requiring human creative judgment. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill promotes persistent browser sessions, login automation, scraping, and anti-bot bypass without enough stated limits or user controls. <br>
Mitigation: Review the skill carefully before installing, use it only for sites and accounts you are authorized to automate, and do not use it for compliant scraping or anti-bot circumvention without stronger guardrails from the publisher. <br>
Risk: Browser automation may expose credentials or session data if the agent stores or reuses authenticated sessions. <br>
Mitigation: Avoid providing credentials unless you understand how the agent stores browser sessions, and prefer scoped test accounts or explicit session cleanup for sensitive workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/bsession) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with JSON examples and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce structured browser automation results, execution logs, extracted page data, and screenshots when supported by the agent environment.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
