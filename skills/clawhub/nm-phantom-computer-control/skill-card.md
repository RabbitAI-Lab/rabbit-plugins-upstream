## Description: <br>
Automates desktop GUI workflows via computer use API with screenshot capture. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and automation engineers use this skill to guide agents through GUI workflows, visual web app testing, form filling, menu navigation, and desktop tasks that require screenshot-based verification. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can capture the visible desktop and may expose private information in screenshots. <br>
Mitigation: Close private applications before use and run the workflow in an isolated desktop, VM, or container when possible. <br>
Risk: Mouse and keyboard automation can cause cross-application side effects or real-world actions. <br>
Mitigation: Require confirmation before destructive or real-world actions and keep the workflow explicitly opt-in. <br>
Risk: Long-running GUI loops can consume API budget or continue after the task stops being useful. <br>
Mitigation: Set iteration caps and monitor execution during automation. <br>
Risk: Supplying sensitive credentials to automated GUI sessions increases account exposure. <br>
Mitigation: Avoid sensitive accounts such as banking and provide login credentials only when necessary. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-phantom-computer-control) <br>
- [Night Market phantom plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/phantom) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration instructions] <br>
**Output Format:** [Markdown with inline bash and Python code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include GUI automation steps, environment checks, API usage examples, and safety guidance.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence; artifact frontmatter says 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
