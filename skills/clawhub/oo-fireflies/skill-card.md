## Description:

Fireflies lets agents read, create, update, and delete Fireflies data through an OOMOL-connected Fireflies account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Fireflies meeting data through OOMOL's connector, including transcript retrieval, AskFred threads, bites, channels, users, privacy, role, and title management.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that could install unverified code if copied directly.

Mitigation: Use an official, versioned installer and verify checksums or signatures before installation.

Risk: The skill can perform high-impact Fireflies changes, including deletes, role changes, privacy changes, and other state-changing actions.

Mitigation: Require explicit user confirmation of the target, payload, and effect before running write or destructive actions.

Risk: Fireflies operations are routed through OOMOL's oo CLI and a connected Fireflies account.

Mitigation: Install only when this routing model is acceptable and review the connected account scopes before use.

## Reference(s):

- [Fireflies homepage](https://www.fireflies.ai)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Fireflies skill page](https://clawhub.ai/oomol/skills/oo-fireflies)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Fireflies icon](https://static.oomol.com/logo/third-party/Fireflies.svg)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection; write and destructive Fireflies actions require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
