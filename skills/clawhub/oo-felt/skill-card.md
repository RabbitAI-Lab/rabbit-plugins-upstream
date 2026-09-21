## Description:

Use Felt (felt.com) to read, create, update, and delete Felt maps and projects through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users use this skill to operate Felt maps and projects through the OOMOL Felt connector, including lookup, creation, updates, duplication, moves, and deletion. The skill is intended for agents handling Felt requests without direct raw API-token handling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can run a remote installer script when the oo CLI is missing.

Mitigation: Install the oo CLI only from a verified official source and review any installer before running it.

Risk: The skill can create, update, move, duplicate, or delete Felt maps and projects.

Mitigation: Fetch the live connector schema first, then confirm the exact target and payload before write or destructive actions.

Risk: Using the skill grants connector-mediated access to a Felt account through OOMOL.

Mitigation: Install only when the publisher is trusted and the user is comfortable granting OOMOL connector access to Felt.

## Reference(s):

- [Felt homepage](https://felt.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before building Felt action payloads; write and destructive actions require explicit user confirmation.]

## Skill Version(s):

1.0.4 (source: evidence release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
