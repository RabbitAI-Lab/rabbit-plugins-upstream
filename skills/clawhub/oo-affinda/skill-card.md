## Description:

Affinda helps an agent read, create, and update Affinda data through an OOMOL-connected account and the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Affinda document workflows from an agent, including uploading documents from URLs, retrieving documents, and listing document types, organizations, and workspaces.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented first-time setup includes remote installer commands that download and execute shell or PowerShell scripts.

Mitigation: Install or inspect the oo CLI through a verified, versioned method before using the skill, and do not let an agent run the installer automatically.

Risk: The document upload action changes Affinda state by submitting a document URL for processing.

Mitigation: Confirm the exact payload and intended effect with the user before running write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-affinda)
- [Affinda Homepage](https://www.affinda.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Agent responses may include oo CLI commands, Affinda action names, schema-inspection steps, JSON request payloads, and setup guidance.]

## Skill Version(s):

1.0.3 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
