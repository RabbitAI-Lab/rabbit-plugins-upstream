## Description:

DocuGenerate operates a connected DocuGenerate account through OOMOL's oo CLI to read, create, update, and delete templates and generated documents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage DocuGenerate templates and generated documents through an OOMOL-connected account, including listing, retrieving, generating, renaming, and deleting documents.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fallback setup recommends running remotely fetched oo CLI installer scripts without verification.

Mitigation: Review the installation path before use and prefer official documentation, versioned packages, or verified downloads.

Risk: The skill can generate, rename, or permanently delete DocuGenerate documents.

Mitigation: Confirm write or destructive actions with the user after checking the exact target and payload.

## Reference(s):

- [DocuGenerate ClawHub skill page](https://clawhub.ai/oomol/skills/oo-docugenerate)
- [DocuGenerate homepage](https://www.docugenerate.com)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)

## Skill Output:

**Output Type(s):** [Shell commands, API Calls, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON payloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs oo connector commands that return JSON responses containing data and meta.executionId.]

## Skill Version(s):

1.0.4 (source: evidence.release.version and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
