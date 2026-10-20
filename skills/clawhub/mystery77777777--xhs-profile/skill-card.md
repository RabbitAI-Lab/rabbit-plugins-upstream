## Description:

Collects public Xiaohongshu creator-profile note lists for content research, returning note details and optional CSV exports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[mystery77777777](https://clawhub.ai/user/mystery77777777)

### License/Terms of Use:

MIT-0

## Use Case:

External users and analysts collect public creator-profile posts for content audits, competitor research, and KOL evaluation, either in batches or page by page.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The default service address transmits reusable account tokens over plaintext HTTP; tokens are also stored locally.

Mitigation: Configure a trusted HTTPS service before login, avoid insecure TLS mode, and protect the local token file.

Risk: Collection and session steps can consume paid credits without CLI-enforced approval.

Mitigation: Check the balance, explain expected charges, and obtain explicit user confirmation before every collect or session step.

## Reference(s):

- [xhs-profile ClawHub release](https://clawhub.ai/mystery77777777/skills/xhs-profile)

## Skill Output:

**Output Type(s):** [Text, Files]

**Output Format:** [JSON responses with optional CSV export]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes note details, task status, and charged or refunded credits.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
