## Description:

Operate HeyGen through an OOMOL-connected account to read, create, update, delete, and generate HeyGen account resources and videos.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage HeyGen resources from an agent session, including account details, quotas, assets, avatars, voices, templates, folders, videos, and video generation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can direct an agent to run oo CLI commands against a connected HeyGen account.

Mitigation: Install and authenticate the oo CLI yourself from a trusted source, then review the proposed command and target account before execution.

Risk: Some supported actions upload assets, start video generation jobs, or delete HeyGen resources.

Mitigation: Require explicit user approval for every state-changing or destructive action, including the exact payload, action name, and affected resource IDs.

Risk: Incorrect JSON payloads could trigger unintended HeyGen operations.

Mitigation: Fetch the live action schema with `oo connector schema` before constructing payloads and verify generated JSON against that schema.

## Reference(s):

- [HeyGen homepage](https://www.heygen.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub HeyGen skill page](https://clawhub.ai/oomol/skills/oo-heygen)

## Skill Output:

**Output Type(s):** [Text, Shell commands, JSON payloads, Configuration guidance]

**Output Format:** [Markdown guidance with bash commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands may return JSON responses from the oo CLI; uploads, video generation, deletions, and other state-changing actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: server release evidence and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
