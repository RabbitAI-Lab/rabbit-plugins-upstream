## Description:

SlickText (slicktext.com). Use this skill for ANY SlickText request: reading, creating, updating, and deleting data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate SlickText through an OOMOL-connected account, including brand lookup and contact creation, retrieval, listing, updates, and deletion. The skill guides the agent to inspect live connector schemas before building JSON payloads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup instructions include remote installer scripts, which can execute unreviewed code if run without validation.

Mitigation: Review the oo CLI installation path, prefer an official versioned source, and verify integrity before running installer scripts.

Risk: Write and destructive SlickText actions can change or delete contact data.

Mitigation: Confirm the exact payload, effect, and target with the user before running create, update, or delete actions.

## Reference(s):

- [SlickText homepage](https://www.slicktext.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [shell commands, guidance, configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the oo CLI to inspect SlickText connector schemas and run actions that return JSON.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
