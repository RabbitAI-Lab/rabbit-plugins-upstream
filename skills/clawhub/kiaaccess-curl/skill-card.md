## Description:

Provides curl-based guidance and request examples for querying Kia vehicle status, location, EV charge state, and remote commands through the Kia Owners API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and technically proficient vehicle owners use this skill to prepare one-off shell commands for reading Kia vehicle state and issuing remote lock, climate, and charging actions without running the related MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can help prepare commands that remotely affect a real Kia vehicle, including unlock, climate, and charging actions.

Mitigation: Require explicit user confirmation before running any vehicle-changing command and re-read vehicle state after execution to verify the intended result.

Risk: The workflow stores an rmtoken that can refresh access to the vehicle account.

Mitigation: Store the token only in the documented session file with restrictive permissions, avoid sharing it, and delete it when access is no longer needed.

## Reference(s):

- [Ready-to-run requests](artifact/references/requests.md)
- [Kia Owners API endpoint](https://api.owners.kia.com/apigw/v1)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/kiaaccess-curl)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash and jq command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes request bodies, header setup, token storage guidance, and verification steps for vehicle actions.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
