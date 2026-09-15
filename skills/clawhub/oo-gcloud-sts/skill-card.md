## Description:

Google Cloud STS support for agents using an OOMOL-connected account to inspect connector schemas and exchange OOMOL OIDC credentials for Google Cloud access tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to run Google Cloud STS connector actions through the oo CLI for a connected OOMOL account, especially to obtain federated Google Cloud access tokens.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can mint and return Google Cloud access tokens.

Mitigation: Confirm token generation with the user, treat returned tokens as secrets, and avoid logging or pasting them into transcripts.

Risk: The artifact includes remote installer commands that pipe downloaded scripts into a shell.

Mitigation: Prefer a verified package-manager or documented install path for the oo CLI before running connector commands.

Risk: The token exchange action is described as read-like even though it returns usable cloud credentials.

Mitigation: Review the live connector schema and exact payload before execution, and handle the result with credential-level safeguards.

## Reference(s):

- [Google Cloud Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Skill page](https://clawhub.ai/oomol/skills/oo-gcloud-sts)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return Google Cloud access tokens that must be treated as secrets.]

## Skill Version(s):

1.0.3 (source: server release metadata; artifact metadata matches)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
