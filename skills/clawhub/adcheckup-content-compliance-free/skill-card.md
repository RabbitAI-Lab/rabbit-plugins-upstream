## Description:

Pre-checks Chinese advertising copy for absolute-language claims and applies exemption logic from advertising enforcement guidance before publication.

This skill is ready for commercial/non-commercial use.

## Publisher:

[chenqg618](https://clawhub.ai/user/chenqg618)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, ecommerce, and bid-document reviewers use this skill to screen Chinese copy for absolute-language advertising claims and see which findings are exempted by the documented guideline logic. It is a pre-check aid and does not replace legal advice or regulator determinations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The artifact includes a paid-upgrade flow and an unpinned third-party install command that could lead an assistant toward payment or package installation.

Mitigation: Use only the local free checker unless the package, source, version, and payment terms are independently verified; require explicit human confirmation before any payment, wallet authorization, or install command.

Risk: The checker produces advertising compliance pre-check results that could be mistaken for a legal or regulator determination.

Mitigation: Treat outputs as review aids and route final compliance decisions to qualified reviewers or the relevant authority.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/chenqg618/skills/adcheckup-content-compliance-free)
- [Publisher profile](https://clawhub.ai/user/chenqg618)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with optional JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports executed checks, withheld checks, findings, exemptions, and insufficient-input status without making a legal determination.]

## Skill Version(s):

1.1.9 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
