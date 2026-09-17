## Description:

Kit (kit.com) requests for reading, creating, and updating data through OOMOL's oo CLI instead of direct Kit API calls.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Kit through OOMOL's connected oo CLI workflows. It supports Kit subscriber, form, landing page, tag, account, and authenticated-user operations, with confirmation expected before write actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes installer commands that execute remote scripts directly on the user's machine.

Mitigation: Review before installing; prefer a verified, pinned, or package-manager installation path when available.

Risk: Write actions can create or update Kit subscriber records.

Mitigation: Confirm the exact payload and expected effect with the user before running create_subscriber or update_subscriber.

## Reference(s):

- [ClawHub Kit Skill](https://clawhub.ai/oomol/skills/oo-kit)
- [Kit Homepage](https://kit.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live Kit connector schema inspection before payload construction and asks for confirmation before write actions.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
