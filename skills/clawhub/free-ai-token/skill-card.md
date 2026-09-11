## Description:

Free Ai helps agents find, compare, and set up free or low-cost AI API keys, free AI products, and AI membership deals with live verification and safety checks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[laowang-ai-xbb](https://clawhub.ai/user/laowang-ai-xbb)

### License/Terms of Use:

MIT

## Use Case:

External users and developers use this skill to research current AI access options, compare free or low-cost API and membership choices, and receive guided setup steps for supported agent clients.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may guide account creation, browser sessions, verification-code handling, API-key setup, and account-related progress tracking.

Mitigation: Prefer manual signup and secure key storage, avoid granting mailbox or payment-detail access, and keep user approval at account or credential gates.

Risk: Cross-region, reseller, or deal-hunting paths can create terms-of-service or account-ban risk.

Mitigation: Prefer official channels, present compliance caveats before action, and stop when a path requires fabricated identity, address, or payment details.

Risk: The release guidance notes an unpinned npx installation path.

Mitigation: Use a pinned or checksum-verified install source when deploying the skill.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/laowang-ai-xbb/skills/free-ai-token)
- [Server-resolved source repository](https://github.com/laowang-ai-xbb/free-ai-token)
- [Safety guidance](references/safety.md)
- [Deal hunting methodology](references/deal-hunting.md)
- [Scoring model](references/scoring.md)
- [Vendor registry](references/vendor-registry.md)
- [Command behavior](references/commands.md)
- [Auto-registration workflow](references/auto-register.md)
- [Membership purchase workflow](references/buy-membership.md)
- [Configuration template](assets/templates/openai-compatible-config.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown, HTML report templates, configuration snippets, and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended to be concise, sourced, date-aware, and separated by delivery form.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact frontmatter and changelog report 2.9.5)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
