## Description:

Guides agents through authorized Atoll planning, project and issue management, execution, local-runner operations, and integrations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[doubledipcode](https://clawhub.ai/user/doubledipcode)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and project teams use this skill to guide an authorized agent through Atoll planning and execution workflows, including issues, goals, milestones, artifacts, and integrations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad Atoll access can change or delete projects, board columns, and integrations.

Mitigation: Use the least-privileged authorized profile; confirm destructive changes and verify the resulting state.

Risk: API credentials or sensitive project context could be exposed in conversations or logs.

Mitigation: Keep real keys in approved local configuration and omit secrets and sensitive payloads from chats, comments, and logs.

Risk: Local-runner installation or resuming execution can affect the user's environment.

Mitigation: Review runner service installation separately and require confirmation before resuming work.

## Reference(s):

- [Atoll skill release](https://clawhub.ai/doubledipcode/skills/atoll-api)
- [Atoll API endpoint reference](references/api-endpoints.md)
- [Atoll authentication and profiles](references/authentication-and-profiles.md)
- [Atoll local runner](references/local-runner.md)
- [Atoll Vercel integration documentation](https://docs.atollhq.com/integrations/vercel)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, API calls]

**Output Format:** [Text or Markdown with commands and structured Atoll responses where applicable]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent actions may change authorized Atoll resources; verify mutations by reading back their state.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
