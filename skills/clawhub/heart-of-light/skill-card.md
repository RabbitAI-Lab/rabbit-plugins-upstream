## Description:

heart-of-light provides an opt-in ethical communication framework for agents, with guidance for honesty, dignity, verification, calm refusal, and self-review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this documentation-only skill as an ethical companion for agent communication, research, code review, writing, data analysis, and hard conversations. It is intended to guide tone, uncertainty handling, verification habits, and refusal behavior after explicit opt-in.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact is documentation-only but describes helper scripts and prompt/config changes that are not present in the published files.

Mitigation: Inspect the installed package before running any referenced command, and do not rely on absent helpers for activation, logging, or configuration changes.

Risk: The security summary flags inconsistent local-only and network statements.

Mitigation: Treat privacy and network claims as unconfirmed until the publisher clarifies them; use least privilege and avoid secrets or network access unless verified.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/heart-of-light)
- [SKILL.md](artifact/SKILL.md)
- [README.md](artifact/README.md)
- [AGENT_DISCOVERY.md](artifact/AGENT_DISCOVERY.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration]

**Output Format:** [Markdown guidance with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Documentation-only; activation is opt-in via HEART_OF_LIGHT_MODE=ON.]

## Skill Version(s):

2.0.13 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
