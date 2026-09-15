## Description:

Short Menu (shortmenu.com) enables an agent to create, update, and delete Short Menu short links through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to manage Short Menu short links from an agent workflow after connecting Short Menu through OOMOL. It supports create, update, and delete actions and requires confirmation before write or destructive changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes a pipe-to-shell installer for the oo CLI, which the security evidence flags as an unverified remote installer pattern.

Mitigation: Install the oo CLI from a verified official package or reviewed download instead of running the pipe-to-shell installer blindly.

Risk: The skill can create, update, and delete Short Menu links, including destructive deletion.

Mitigation: Require explicit user confirmation of the target, payload, and expected effect before write or destructive actions.

## Reference(s):

- [Short Menu ClawHub listing](https://clawhub.ai/oomol/skills/oo-short-menu)
- [Short Menu homepage](https://shortmenu.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: frontmatter and server evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
