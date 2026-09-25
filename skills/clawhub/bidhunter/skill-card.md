## Description:

BidHunter helps agents monitor public tender notices, compare opportunities against local qualification rules, generate bid-readiness reports, scan tender or bid documents for legal red flags, and run a local pre-bid quote gate.

This skill is ready for commercial/non-commercial use.

## Publisher:

[419597334-sudo](https://clawhub.ai/user/419597334-sudo)

### License/Terms of Use:

MIT-0

## Use Case:

Business development, bid operations, and tender compliance teams use this skill to collect tender notices, triage whether opportunities are worth pursuing, prepare review reports, and check bid documents or pricing inputs before submission.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Tender documents, qualification rules, local credentials, and bid strategy inputs may be sensitive; AI modes can send extracted tender text to MiniMax through the user's configured API key.

Mitigation: Use local-only modes for confidential bid files unless the organization has approved MiniMax for that data, and keep local configuration files protected.

Risk: The security evidence flags generated HTML reports and the local rule editor as areas users should review before installation.

Mitigation: Avoid opening generated HTML from untrusted feeds, review report content before sharing, and run the rule editor only when needed rather than leaving it open during unrelated browsing.

Risk: Bid-source scraping can miss notices when upstream platforms change authentication, paths, or availability.

Mitigation: Check source health with the provided diagnostics and platform guidance, disable broken adapters, and add custom sources for platforms that require current access paths.

## Reference(s):

- [BidHunter Configuration Guide](references/setup-guide.md)
- [Supported Platforms and Configuration](references/platforms.md)
- [Filter Rule Structure and Dimensions](references/filter_rules.md)
- [Tender Field Standardization Schema](references/field_standard.md)
- [MiniMax Product Home](https://www.minimaxi.com/)
- [MiniMax Open Platform Login](https://platform.minimaxi.com/login)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown and command-oriented guidance, with generated text reports, HTML reports, JSON-capable scan output, and local configuration files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are generated locally; optional AI features may call MiniMax with the user's configured API key.]

## Skill Version(s):

2.7.0 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
