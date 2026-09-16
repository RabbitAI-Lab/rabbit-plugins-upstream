## Description:

Checks Huawei Cloud real-name verification status and guides face-scan verification read-only through hcloud while refusing writes and sensitive identity intake.

This skill is ready for commercial/non-commercial use.

## Publisher:

[agenticweb4](https://clawhub.ai/user/agenticweb4)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and cloud operators use this skill to check whether a Huawei Cloud account can purchase resources and, when needed, guide the account holder through the documented face-scan QR verification flow without collecting identity documents or credentials.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill handles a sensitive face-verification QR URL that functions as a one-time credential.

Mitigation: Render only QR URLs produced by the documented hcloud command for the current account, do not share or log the URL, and never persist, forward, or reuse it.

Risk: The QR operation may return a usable code even when the account is already verified.

Mitigation: Run ShowRealNameAuthStatus before every QR request and short-circuit verified or pending accounts instead of fetching another code.

Risk: Using npx directly can fetch packages dynamically at execution time.

Mitigation: Prefer a locked local install from the bundled package-lock.json before running the QR renderer.

## Reference(s):

- [Command Contract](references/commands.md)
- [Real-Name Verification Concepts](references/concepts.md)
- [Terminal QR Renderer](scripts/render-qr.ts)
- [ClawHub Skill Page](https://clawhub.ai/agenticweb4/skills/huawei-cloud-account-onboarding)
- [Project Homepage](https://github.com/concept-git/cloud-concept-skills/tree/main/skills/en/huawei-cloud-account-onboarding)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline bash code blocks and status-routing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include a terminal QR rendering command for a one-time face-verification URL; no generated files are required by the skill itself.]

## Skill Version(s):

1.0.2 (source: server release metadata; skill frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
