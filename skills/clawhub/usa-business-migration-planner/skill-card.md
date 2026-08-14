## Description:

Helps maintainers and users create repeatable workflows, checklists, analysis, code, and validation notes for adding TOTP and WebAuthn multi-factor authentication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kyro-ma](https://clawhub.ai/user/kyro-ma)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, maintainers, and users use this skill to turn MFA implementation requests into practical plans, checklists, code changes, or decision support for adding TOTP and WebAuthn. It is intended to produce actionable work products while making assumptions, limits, and follow-up validation visible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill name and visible business-migration framing do not match the MFA, TOTP, and WebAuthn workflow content, which may confuse users or lead to incorrect invocation.

Mitigation: Rename or rewrite the skill before relying on it, and make the public title, summary, triggers, and instructions consistently describe MFA implementation planning.

Risk: The release enables broad implicit invocation despite the name/content mismatch.

Mitigation: Disable implicit invocation or tightly scope triggers to MFA, TOTP, WebAuthn, and authentication-planning requests until the package is corrected.

Risk: Authentication implementation guidance can lead to insecure outcomes if produced without domain-specific review.

Mitigation: Require security review for generated MFA plans or code, including recovery flows, phishing-resistant WebAuthn posture, secret handling, and rollout controls.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/kyro-ma/skills/usa-business-migration-planner)
- [Requirement Plan](references/requirement-plan.md)
- [Add TOTP and WebAuthn multi-factor authentication](https://github.com/halfsend/eval-006-not-planned-guardrail-53644ef4/issues/1)
- [FIDO2 WebAuthn integration issue](https://github.com/SandeepVashishtha/Eventra/issues/17944)
- [WebAuthn identity protection article](https://segmentfault.com/a/1190000043210024)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with optional code blocks, checklists, implementation notes, and verification notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include tailored assumptions, remaining risks, and follow-up work.]

## Skill Version(s):

0.20260814.40500 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
