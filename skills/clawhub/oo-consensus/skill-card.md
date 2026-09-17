## Description:

Consensus (consensus.app) lets an agent search and read academic research through the OOMOL-connected Consensus connector instead of calling the service API directly.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to search Consensus for relevance-ranked academic papers with publication, study, and quality filters through an authenticated OOMOL account connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes remote installer commands that pipe downloaded scripts directly to a shell.

Mitigation: Install the oo CLI through a verified release or package process and review installer contents before execution.

Risk: The skill uses an OOMOL account connection to access Consensus, so authentication and connected-service permissions affect what actions can run.

Mitigation: Review sign-in and connection prompts before proceeding, and run setup steps only after an authentication or connection error requires them.

## Reference(s):

- [Consensus homepage](https://consensus.app)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return connector JSON responses containing data and execution metadata.]

## Skill Version(s):

1.0.2 (source: server release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
