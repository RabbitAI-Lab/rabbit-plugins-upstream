## Description:

NiftyImages helps agents inspect live connector schemas and run NiftyImages read operations through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers with connected OOMOL and NiftyImages accounts use this skill to retrieve image, widget, user, impression, and aggregate statistics through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup can direct an agent or user to execute mutable remote installer scripts.

Mitigation: Review the skill before installing, verify the oo CLI source, and do not allow an agent to run remote installer commands automatically.

Risk: Signing in or connecting NiftyImages through OOMOL may create persistent account access for future connector calls.

Mitigation: Connect only trusted accounts, review requested scopes, and revoke or refresh the connection when access is no longer needed.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-niftyimages)
- [NiftyImages Homepage](https://niftyimages.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before action execution and returns connector results as JSON when run with --json.]

## Skill Version(s):

1.0.3 (source: release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
