## Description:

Google Cloud STS helps an agent request a Google Cloud Workload Identity Federation access token through an OOMOL-connected gcloud_sts account using the oo CLI.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill when an agent needs Google Cloud STS access through an OOMOL-connected account. It guides the agent to inspect the live connector schema, build a matching JSON payload, and run the token-exchange action through the oo CLI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can request a Google Cloud federated access token, and any returned token is sensitive.

Mitigation: Use the skill only when token issuance is intended, review commands before execution, and avoid exposing returned tokens in logs or shared transcripts.

Risk: The security guidance flags the first-time CLI installation commands as risky when used without pinning or verification.

Mitigation: Prefer pinned, verified oo CLI installation paths and organization-approved package management before enabling the skill.

Risk: The security summary says sensitive token handling is under-disclosed for this token-exchange workflow.

Mitigation: Review the skill before installation and document local handling expectations for Google Cloud access tokens returned by the connector.

## Reference(s):

- [Google Cloud Workload Identity Federation](https://cloud.google.com/iam/docs/workload-identity-federation)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON payload examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Connector runs return JSON data with execution metadata when actions are executed.]

## Skill Version(s):

1.0.3 (source: server evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
