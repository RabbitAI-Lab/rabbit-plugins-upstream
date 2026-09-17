## Description:

Nutrient DWS helps an agent operate Nutrient Document Web Services through an OOMOL-connected account for reading account information, estimating Build API credit use, and creating or revoking JWT auth tokens.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to manage Nutrient DWS through the OOMOL connector, including schema inspection, Build API credit estimation, connected-account checks, and scoped JWT token lifecycle actions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The setup path includes remote installer commands that can execute arbitrary code.

Mitigation: Review and verify the OOMOL installer before use, or prefer a pinned, signed, or package-manager installation method for the oo CLI.

Risk: Some connector actions can change or remove Nutrient DWS resources, including JWT auth tokens.

Mitigation: Confirm write payloads and destructive targets with the user before running create_auth_token or delete_auth_token.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/oomol/skills/oo-nutrient-document-web-services-api)
- [OOMOL publisher profile](https://clawhub.ai/user/oomol)
- [Nutrient DWS homepage](https://www.nutrient.io/api/)
- [oo CLI](https://github.com/oomol-lab/oo-cli)
- [Skill icon](https://static.oomol.com/logo/third-party/nutrient_document_web_services_api.svg)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Configuration]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schemas before constructing action payloads; responses are JSON objects with data and meta.executionId.]

## Skill Version(s):

1.0.2 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
