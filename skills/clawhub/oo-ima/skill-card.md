## Description:

ima lets an agent read, create, and update ima notes and knowledge-base content through the OOMOL oo CLI connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to operate Tencent ima through an OOMOL-connected account, including note workflows, knowledge-base browsing, search, imports, and uploads.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path can execute remote installer scripts for the oo CLI.

Mitigation: Install the oo CLI only from a trusted, verified source, review installer scripts before execution, and avoid pipe-to-shell installation when possible.

Risk: Write actions can create notes, append content, import URLs, upload files, or add items to knowledge bases.

Mitigation: Confirm the exact action, target, payload, and user-visible effect before allowing any write action to run.

Risk: Connector payloads may be invalid or stale if generated without checking the current schema.

Mitigation: Fetch the live action schema with the oo CLI before constructing or submitting each payload.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-ima)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [ima homepage](https://ima.qq.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The skill asks the agent to fetch the live connector schema before building action payloads.]

## Skill Version(s):

1.0.5 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
