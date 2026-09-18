## Description:

Autoblogging.ai helps agents inspect live action schemas and operate Autoblogging.ai article creation and status retrieval through the OOMOL oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to create Autoblogging.ai article-generation jobs and fetch article status through an OOMOL-connected account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup includes remote installer commands that could execute unverified code if run automatically.

Mitigation: Install the oo CLI manually from official documentation, verify the installer source, and do not let an agent run curl|bash or irm|iex automatically.

Risk: The create_article action changes Autoblogging.ai state and may consume credits.

Mitigation: Inspect the live action schema and confirm the exact article-creation payload and expected effect before allowing write actions.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-autoblogger)
- [Autoblogging.ai Homepage](https://autoblogging.ai)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires live action schema inspection before constructing connector payloads.]

## Skill Version(s):

1.0.2 (source: server evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
