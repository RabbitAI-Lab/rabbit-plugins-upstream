## Description:

Gamma (gamma.app) helps agents read, create, and update Gamma data through the OOMOL-connected oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to operate Gamma through an OOMOL-connected account, including creating and polling generation jobs, checking status, retrieving result URLs, and listing folders or themes. It is intended for users who have the oo CLI installed and a connected Gamma account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup documents remote installer commands that pipe downloaded scripts directly into a shell.

Mitigation: Review and verify OOMOL installer sources before execution, or prefer a signed, pinned, or package-manager installation path for the oo CLI.

Risk: Write actions can create Gamma generations or otherwise change Gamma workspace state.

Mitigation: Confirm the exact action payload and expected effect with the user before running actions tagged as write.

## Reference(s):

- [ClawHub Gamma skill page](https://clawhub.ai/oomol/skills/oo-gamma)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Gamma homepage](https://gamma.app)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
