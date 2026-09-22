## Description:

Provides curl-based SignUpGenius session access for reading and managing sign-ups, groups, RSVPs, and slot workflows without running the signupgenius-mcp server.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chrischall](https://clawhub.ai/user/chrischall)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to issue SignUpGenius API and legacy dispatcher requests from shell scripts, including login, profile, group, sign-up, RSVP, slot, claim, and release workflows. It is intended for users who need direct curl workflows instead of installing or running an MCP server.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires SignUpGenius credentials and session cookies that can expose account access if stored insecurely.

Mitigation: Use a secrets manager, avoid shared machines, restrict temporary files, and delete cookie or header files after use.

Risk: The skill can read participant and contact information from SignUpGenius workflows, including unauthenticated public participant endpoints described in the artifact.

Mitigation: Review whether the target sign-up permits this access, limit use to authorized workflows, and avoid retaining personal data longer than necessary.

Risk: The skill includes write workflows for adding members, submitting RSVPs, claiming slots, and releasing slots.

Mitigation: Require explicit user confirmation before any write, RSVP, claim, release, or withdrawal action and verify the target account or participant before execution.

## Reference(s):

- [SignUpGenius session-mode endpoints for curl](references/sug-endpoints.md)
- [ClawHub skill page](https://clawhub.ai/chrischall/skills/signupgenius-api)
- [Publisher profile](https://clawhub.ai/user/chrischall)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Code, Configuration]

**Output Format:** [Markdown with inline shell commands, curl examples, jq recipes, JSON payloads, and implementation notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces agent guidance for executing SignUpGenius read and write workflows; external command results depend on the user's account, permissions, and live SignUpGenius responses.]

## Skill Version(s):

2.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
