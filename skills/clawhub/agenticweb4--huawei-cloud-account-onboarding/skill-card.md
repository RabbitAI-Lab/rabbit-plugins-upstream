## Description:

Checks Huawei Cloud real-name verification status and guides the account holder through read-only face-scan verification using hcloud.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Huawei Cloud account holders and cloud operators use this skill to check current real-name verification status and, when needed, complete the face-scan flow on the account holder’s phone. It provides read-only status guidance and does not handle identity documents or credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The face-verification QR URL contains a one-time ticket and may be exposed in terminal output.

Mitigation: Fetch it only when the account holder is ready to scan, verify the returned hostname is auth.huaweicloud.com, and keep the QR code and output private; do not persist, forward, or reuse the URL.

Risk: Misconfigured or unexpectedly modified CLI dependencies or credentials could expose account access.

Mitigation: Have the user configure hcloud credentials themselves, use reviewed and locked dependencies, and avoid unexpected runtime downloads.

## Reference(s):

- [Command reference](references/commands.md)
- [Verification concepts](references/concepts.md)
- [Project homepage](https://github.com/concept-git/cloud-concept-skills/tree/main/skills/en/huawei-cloud-account-onboarding)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Terminal QR code]

**Output Format:** [Text with shell commands and a terminal-rendered QR code]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [A QR code URL is a one-time credential; keep it private and do not persist or forward it.]

## Skill Version(s):

1.0.3 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
