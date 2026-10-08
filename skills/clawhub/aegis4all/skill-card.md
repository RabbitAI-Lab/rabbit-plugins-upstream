## Description:

Aegis4All helps OpenClaw users audit security settings, review proposed fixes, add persistent safety rules with approval, and follow plain-language hardening guides.

This skill is ready for commercial/non-commercial use.

## Publisher:

[xiaozheng-jc](https://clawhub.ai/user/xiaozheng-jc)

### License/Terms of Use:

MIT-0

## Use Case:

OpenClaw users and administrators use this skill to inspect configuration and workspace security, get a scored audit with suggested actions, and review optional hardening guidance and persistent rules.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Injecting rules changes the agent's persistent behavior.

Mitigation: Review the exact rule block and approve each write to AGENTS.md or TOOLS.md before applying it.

Risk: Applying proposed configuration fixes without review can disrupt access or change security settings.

Mitigation: Run the read-only audit first, inspect proposed fixes, and confirm each change before it is applied.

## Reference(s):

- [Aegis4All on ClawHub](https://clawhub.ai/xiaozheng-jc/skills/aegis4all)
- [Understanding and mitigating the risks of OpenClaw for non-technical users](https://arxiv.org/abs/2606.11007)
- [Aegis4All security guide](artifact/guides/security-guide.md)
- [Aegis4All persistent safety rules](artifact/rules/inject.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance]

**Output Format:** [Plain-language Markdown audit reports, recommendations, and step-by-step guides]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Audit reports score 20 checkpoints; proposed fixes and persistent rule changes require user confirmation.]

## Skill Version(s):

4.0.2 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
