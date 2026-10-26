## Description:

Checks Huawei Cloud real-name verification status and guides face-scan verification read-only through hcloud without accepting identity documents, bank details, or SMS codes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

External Huawei Cloud users and cloud operators use this skill to check whether the current account can purchase resources and, when needed, guide the account holder through a read-only face-scan verification flow.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The QR helper can render non-Huawei links and prints a one-time verification URL in terminal output.

Mitigation: Render only URLs produced directly by hcloud ShowRealNameAuthQrCode for the current Huawei Cloud account, avoid copied or user-supplied URLs, and treat the printed manual URL as a sensitive one-time credential.

Risk: Credential handling could expand beyond the intended read-only flow if an agent tries to configure hcloud on the user's behalf.

Mitigation: Require the user to configure their own hcloud profile and refuse to accept, write, or replace access keys, identity documents, bank details, or SMS codes.

Risk: Fetching QR codes without checking status can expose unnecessary verification URLs, including for already verified accounts.

Mitigation: Run ShowRealNameAuthStatus before each QR request, fetch a QR code only for unverified accounts with the user present, and ask before requesting a replacement after timeout.

Risk: Unpinned or unexpected dependency execution can make the local QR rendering step harder to review.

Mitigation: Use deterministic dependency installation and a local pinned tsx invocation before running the renderer.

## Reference(s):

- [Command Contract](references/commands.md)
- [Real-Name Verification Concepts](references/concepts.md)
- [Terminal QR Renderer](scripts/render-qr.ts)
- [Source Homepage](https://github.com/concept-git/cloud-concept-skills/tree/main/skills/en/huawei-cloud-account-onboarding)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline hcloud and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include terminal QR rendering guidance for a one-time verification URL; does not collect or store identity documents.]

## Skill Version(s):

1.0.2 (source: server release evidence; artifact metadata version 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
