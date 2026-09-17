## Description:

Affinda lets an agent operate Affinda through an OOMOL-connected account using the oo CLI to upload documents, retrieve document data, and list Affinda resources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to perform Affinda document-processing actions through an OOMOL-connected account, including uploads from URLs, document retrieval, and organization, workspace, document type, and document listing workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The fallback setup recommends executing remote installer scripts directly in a shell.

Mitigation: Use a verified official package, pinned release, or downloaded installer that can be inspected and validated before execution.

Risk: Affinda actions and document-related payloads pass through OOMOL as an intermediary.

Mitigation: Install and use the skill only when that intermediary role is acceptable for the intended documents, account, and data-handling requirements.

## Reference(s):

- [ClawHub Affinda skill page](https://clawhub.ai/oomol/skills/oo-affinda)
- [Affinda homepage](https://www.affinda.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands can return JSON responses from Affinda actions through OOMOL, including data and execution metadata.]

## Skill Version(s):

1.0.3 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
