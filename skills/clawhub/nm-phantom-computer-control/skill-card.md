## Description:

Automates desktop GUI workflows via computer use API with screenshot capture.

This skill is ready for commercial/non-commercial use.

## Publisher:

[athola](https://clawhub.ai/user/athola)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and automation engineers use this skill to drive GUI-based workflows, visually test applications, fill forms, navigate desktop apps, and verify screen state when CLI or API automation is not available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can view the screen and control mouse and keyboard in a desktop session.

Mitigation: Install only when desktop control is intended, run it in an isolated VM, container, or dedicated display, and close private windows before use.

Risk: Automated GUI actions may affect accounts, files, or services with real-world consequences.

Mitigation: Require human confirmation before sensitive actions, avoid banking or other sensitive accounts, and use iteration caps to limit runaway activity and API costs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-phantom-computer-control)
- [Project homepage from ClawHub metadata](https://github.com/athola/claude-night-market/tree/master/plugins/phantom)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline bash and Python code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include environment checks, desktop automation commands, API usage examples, and safety guidance.]

## Skill Version(s):

1.9.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
