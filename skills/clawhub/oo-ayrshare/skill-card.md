## Description:

Ayrshare enables agents to read, create, update, validate, schedule, retry, analyze, and delete social posts through an OOMOL-connected Ayrshare account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to operate Ayrshare social publishing workflows from an agent, including profile lookup, post validation, publishing or scheduling, analytics, retries, updates, and deletion.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes running a remote oo CLI installer script on the user's machine.

Mitigation: Install only after trusting OOMOL and the installer source; prefer reviewing the installer or using official documented package-manager steps before running it.

Risk: The skill can publish, update, retry, or delete Ayrshare posts.

Mitigation: Require explicit confirmation of the target, payload, and expected effect before write or destructive actions.

## Reference(s):

- [ClawHub Ayrshare Skill](https://clawhub.ai/oomol/skills/oo-ayrshare)
- [Ayrshare Homepage](https://www.ayrshare.com/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [OOMOL CLI Install Guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live oo connector schemas and may return connector JSON responses when actions are run.]

## Skill Version(s):

1.0.6 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
