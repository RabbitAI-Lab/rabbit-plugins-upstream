## Description:

Neon (neon.com). Use this skill for ANY Neon request: reading, creating, updating, and deleting data through OOMOL's Neon connector instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Neon projects, branches, databases, operations, and current-user information through an authenticated OOMOL-connected account. It supports read workflows and governed write or destructive workflows when the user confirms the exact target and payload.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can create, update, and delete Neon resources through the user's connected OOMOL account.

Mitigation: Confirm the exact target, payload, and expected effect before approving write actions, and require explicit user approval before destructive actions.

Risk: The security review flags fallback setup guidance that tells agents to execute remote installer commands directly.

Mitigation: Install the oo CLI only through a trusted, verifiable process, and do not allow an agent to run remote installer commands automatically.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-neon)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Neon homepage](https://neon.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent output may include live connector schema checks, oo CLI connector commands, JSON payloads, and confirmation guidance for write or destructive actions.]

## Skill Version(s):

1.0.3 (source: evidence.release.version and artifact frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
