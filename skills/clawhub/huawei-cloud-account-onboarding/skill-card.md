## Description:

Checks Huawei Cloud real-name verification status and guides face-scan verification through read-only hcloud commands, rendering a one-time QR code for the user to scan by phone and polling until the account is verified.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

External users and cloud operators use this skill when a Huawei Cloud account needs real-name verification before purchasing resources. The skill checks the account status, shows the face-scan QR flow only when appropriate, and avoids collecting identity documents, bank card details, or SMS codes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may paste identity documents, bank card details, or SMS codes into chat during a verification workflow.

Mitigation: The skill refuses those materials, tells the user to delete them, and keeps verification actions on the user's phone.

Risk: A face-verification QR URL is a one-time credential that could be exposed if saved, logged, forwarded, or reused.

Mitigation: The skill renders the QR code for the current user, treats the URL as single-use, and avoids persistent storage or forwarding.

Risk: The agent uses the user's configured Huawei Cloud hcloud profile.

Mitigation: The skill limits execution to the read-only real-name status and QR-code commands and refuses write operations or credential setup.

## Reference(s):

- [Real-Name Verification Concepts](references/concepts.md)
- [Huawei Cloud BSS Command Contracts](references/commands.md)
- [Terminal QR Renderer](scripts/render-qr.ts)
- [Clawdis Homepage](https://github.com/ontology-of-everything/SemanticSkills/tree/main/skills/huawei-cloud-account-onboarding)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration guidance]

**Output Format:** [Markdown with inline hcloud and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only status and QR-code guidance; one-time QR URLs are rendered for the current user and are not meant for persistent output.]

## Skill Version(s):

1.0.0 (source: server release metadata and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
