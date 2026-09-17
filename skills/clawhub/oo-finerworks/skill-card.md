## Description:

FinerWorks (finerworks.com). Use this skill for FinerWorks search and read requests through an OOMOL-connected account.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to inspect FinerWorks action schemas and run read-focused connector actions for pricing, media types, product types, and style types through the OOMOL oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Setup guidance includes internet-downloaded installer commands executed directly in a shell.

Mitigation: Review the installer path before use, prefer verified official release documentation or signed/package-manager installation routes, and avoid pipe-to-shell installation unless the remote endpoint is trusted.

Risk: Connector requests may fail when the oo CLI is not installed, the user is not signed in, or the FinerWorks connection is missing or expired.

Mitigation: Run setup or connection steps only after a matching command failure and keep credentials managed through the OOMOL connection flow.

## Reference(s):

- [FinerWorks homepage](https://finerworks.com/)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-finerworks)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs read-focused FinerWorks connector actions through the oo CLI after inspecting live action schemas.]

## Skill Version(s):

1.0.2 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
