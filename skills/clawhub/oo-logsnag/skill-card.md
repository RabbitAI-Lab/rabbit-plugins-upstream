## Description:

LogSnag (logsnag.com). Use this skill for ANY LogSnag request - reading, creating, and updating data. Whenever a task involves LogSnag, use this skill instead of calling the API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate LogSnag through an OOMOL-connected account, including inspecting live action schemas, updating user properties, publishing project events, and publishing or mutating real-time insight values.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change LogSnag data, including user properties, project events, and insight values.

Mitigation: Confirm the exact payload and effect with the user before running identify_user, mutate_insight, publish_event, or publish_insight.

Risk: The setup guidance includes remote installer commands that could be unsafe if run blindly.

Mitigation: Install the oo CLI through a verified method and avoid executing shell-piped installers without review.

Risk: The agent operates a connected LogSnag account through OOMOL.

Mitigation: Use a least-privilege LogSnag connection where possible and install only when account-level access through OOMOL is acceptable.

## Reference(s):

- [LogSnag homepage](https://logsnag.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing LogSnag requests.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
