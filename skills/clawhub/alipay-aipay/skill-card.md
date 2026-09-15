## Description:

Helps developers integrate Alipay AI pay-as-you-go, AI web app payment, and AI mobile app payment flows, including code development, product onboarding, or both.

This skill is ready for commercial/non-commercial use.

## Publisher:

[alipay](https://clawhub.ai/user/alipay)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to add supported Alipay payment products to applications, prepare sandbox or production configuration, and complete related Alipay product onboarding tasks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill has high authority because it can change user projects, use Alipay CLI credentials, and submit account or product operations.

Mitigation: Run it in a sandboxed or reviewed environment, confirm the project path and operation scope before use, and review generated payment code and Alipay-side changes before production.

Risk: Server security evidence reports automatic self-update and Alipay CLI installation paths that execute unpinned remote code.

Mitigation: Install only after reviewing the publisher release, or require pinned, verified, user-approved update and install steps before deployment.

Risk: Telemetry is enabled by default and can identify the machine over time.

Mitigation: Set ALIPAY_AIPAY_TELEMETRY=0, false, off, or no in environments where telemetry is not approved.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/alipay/skills/alipay-aipay)
- [Alipay Open Platform](https://open.alipay.com/)
- [Runtime entry and support scope](references/runtime-entry.md)
- [Integration flow](references/integration/flow.md)
- [Onboarding flow](references/onboarding/flow.md)
- [Interface guide and code example routing](references/integration/modules/interface-guide.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with code snippets, shell commands, and configuration instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce project edits and Alipay onboarding actions after the skill's required confirmations and checks.]

## Skill Version(s):

1.6.9 (source: server release evidence; artifact VERSION reports 1.6.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
