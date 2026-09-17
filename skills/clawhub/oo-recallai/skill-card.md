## Description:

Recall.ai enables agents to read, create, update, and delete Recall.ai bot and media data through OOMOL's oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and operations teams use this skill to manage Recall.ai meeting bots through an OOMOL-connected account, including scheduling bots, retrieving and listing bot status, removing active bots, and deleting completed bot media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes remote installer commands that can execute code on the user's machine.

Mitigation: Review the installer path first and prefer a signed, versioned, or package-managed oo CLI install source before running installer commands.

Risk: Write or destructive Recall.ai actions can create bots, remove active bots from meetings, or delete completed bot media.

Mitigation: Verify the exact bot, media, meeting target, payload, and intended effect with the user before approving state-changing actions.

Risk: Connector action inputs may differ from assumptions in a prompt or previous run.

Mitigation: Inspect the live Recall.ai action schema before constructing each payload.

## Reference(s):

- [ClawHub Recall.ai Skill Page](https://clawhub.ai/oomol/skills/oo-recallai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)
- [Recall.ai Homepage](https://www.recall.ai)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Recall.ai action schemas before payload construction and requires confirmation for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: server evidence, release metadata, and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
