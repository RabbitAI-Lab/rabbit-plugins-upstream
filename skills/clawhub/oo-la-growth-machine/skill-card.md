## Description:

Operate La Growth Machine through an OOMOL-connected account to read, create, and update audiences, leads, and members using the oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operators use this skill to manage La Growth Machine data from an agent session, including audience creation and listing, lead create/update/search, and member listing. Confirm exact payloads before write actions that change account state.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup includes pipe-to-shell installer commands that execute remote scripts.

Mitigation: Prefer verified official packages or reviewed installers before installing the oo CLI.

Risk: Write actions can create or update La Growth Machine audiences and leads.

Mitigation: Confirm the exact payload and intended account changes with the user before running write actions.

## Reference(s):

- [La Growth Machine homepage](https://lagrowthmachine.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-la-growth-machine)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector responses are JSON objects containing data and meta.executionId when actions run.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
