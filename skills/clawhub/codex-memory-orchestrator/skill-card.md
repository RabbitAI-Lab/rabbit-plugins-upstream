## Description:

Provides long-conversation memory workflows for checking turn and token use, preparing recovery packs, handing off work, and archiving sessions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[lisong2003-lgtm](https://clawhub.ai/user/lisong2003-lgtm)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent users can checkpoint long-running tasks, prepare concise recovery packs, and continue work in a new conversation. Monitoring requires an explicit invocation or scheduled scan and does not guarantee per-turn checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags handoff claims of preapproval and broad triggers that could lead workflows to proceed without clear confirmation.

Mitigation: Review each proposed handoff and confirm the action, project scope, and any conversation content to be read before proceeding; treat generated preapproval claims as unconfirmed.

Risk: The security review reports a purpose mismatch and incomplete coverage, so the available review does not establish that every behavior is covered.

Mitigation: Inspect the packaged files and verify that enabled features match the intended memory-management use before relying on the skill.

## Reference(s):

- [Agent handoff guide](artifact/references/agent-gateways.md)
- [Conversation monitoring guide](artifact/references/monitor-dialogs.md)
- [Step orchestration guide](artifact/references/step-orchestrator.md)
- [Recovery pack templates](artifact/references/templates.md)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, JSON configuration]

**Output Format:** [Recovery-pack Markdown, shell commands, and JSON state or plan data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on the requested project, conversation, and checkpoint task.]

## Skill Version(s):

1.9.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
