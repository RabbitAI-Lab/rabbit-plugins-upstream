## Description:

V2EX (v2ex.com). Use this skill for V2EX requests that read, create, update, or delete data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to operate V2EX through an OOMOL-connected account, including reading topics, replies, nodes, notifications, profiles, and token metadata. With explicit confirmation, it can also run state-changing actions such as boosting topics, setting sticky topics, creating tokens, and deleting notifications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup path recommends executing remote installer scripts for the oo CLI.

Mitigation: Review the installer path before installation and prefer a verified, versioned release or package manager.

Risk: The skill can run write or destructive V2EX actions, including token creation, topic boost or sticky changes, and notification deletion.

Mitigation: Confirm the exact payload and effect with the user before allowing any write, token creation, boost, sticky, or notification deletion action.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-v2ex)
- [OOMOL Publisher Profile](https://clawhub.ai/user/oomol)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [V2EX Homepage](https://www.v2ex.com)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
