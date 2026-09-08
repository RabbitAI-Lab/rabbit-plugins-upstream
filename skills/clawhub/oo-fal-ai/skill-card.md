## Description:

fal.ai (fal.ai). Use this skill for ANY fal.ai request - reading, creating, and updating data. Whenever a task involves fal.ai, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate fal.ai through an OOMOL-connected account, including model discovery, pricing lookup, queue submission, queue status tracking, result retrieval, cancellation, and webhook JWKS retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queue submissions and cancellations can change fal.ai state or incur costs.

Mitigation: Review the exact payload and expected effect with the user before approving write or cancellation actions.

Risk: The skill depends on an OOMOL-connected fal.ai account and local oo CLI availability.

Mitigation: Use first-time setup steps only after an authentication, connection, scope, billing, or missing-command failure.

## Reference(s):

- [fal.ai homepage](https://fal.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-fal-ai)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, Markdown, JSON]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill guides agents to inspect live connector schemas before forming payloads and to confirm write or cancellation actions before execution.]

## Skill Version(s):

1.0.2 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
