## Description:

MOCO (mocoapp.com). Use this skill for MOCO requests that search and read company, contact, and user profile data through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve MOCO companies, contacts, and profile information through the OOMOL oo CLI after their account and MOCO connection are configured.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that could execute arbitrary code if run without inspection.

Mitigation: Install the oo CLI only from a verified package or documented installer that can be inspected first, and avoid running installer commands from an elevated shell.

Risk: MOCO actions depend on a signed-in OOMOL account and a connected MOCO credential.

Mitigation: Run authentication or connection setup only after a command fails with an auth or connection error, and keep credentials managed server-side through OOMOL.

## Reference(s):

- [MOCO homepage](https://www.mocoapp.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-moco)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill retrieves MOCO data through read-oriented connector actions and may return JSON responses from the oo CLI.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
