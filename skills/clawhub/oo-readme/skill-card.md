## Description:

ReadMe helps agents operate ReadMe through an OOMOL-connected oo CLI account for reading, creating, updating, and deleting ReadMe content.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and documentation maintainers use this skill to manage ReadMe docs, categories, changelogs, custom pages, project versions, API specifications, search, metadata, and Owlbot questions through an agent workflow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Remote installer snippets can execute changing code on the user's machine.

Mitigation: Install the oo CLI through a reviewed, trusted, versioned method, and do not allow the agent to run curl-to-bash or PowerShell iex installers automatically.

Risk: Write and destructive actions can create, update, or delete ReadMe content.

Mitigation: Fetch the live action schema, present the exact payload and target, and require explicit user confirmation before write or destructive actions.

Risk: OOMOL mediates ReadMe actions and can enable account-backed changes after confirmation.

Mitigation: Install only when comfortable with OOMOL mediation, connect ReadMe with appropriate scopes, and monitor account access and billing state.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-readme)
- [ReadMe Homepage](https://readme.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads or results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Fetches live action schemas before constructing payloads; write and destructive ReadMe changes require user confirmation.]

## Skill Version(s):

1.0.3 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
