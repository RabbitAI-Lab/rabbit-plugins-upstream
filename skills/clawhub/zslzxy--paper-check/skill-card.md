## Description:

论文查重与 AIGC 报告助手 helps users choose VIP, Wanfang, and CNKI paper-checking products, interpret similarity and AIGC reports, verify report authenticity, count characters, and hand off unpaid orders to the original service pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zslzxy](https://clawhub.ai/user/zslzxy)

### License/Terms of Use:

MIT-0

## Use Case:

Students, researchers, and academic support staff use this skill for Chinese-language guidance on manuscript similarity checks, AIGC detection, character counting, report interpretation, and official report verification. When a user confirms the task and file use, the skill can create or query unpaid orders and return the original service pages for payment, progress, and report handoff.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send selected manuscript files to configured CQCCJY or Fanyu paper-checking services.

Mitigation: Confirm the user's intended brand, product, and file use before upload, and do not upload when the user only asks conceptual or product-selection questions.

Risk: Users may confuse an unpaid draft or order handoff with completed paid detection.

Mitigation: State the current order status clearly, leave payment to the original service page, and avoid claiming that a report is complete until the service returns a completed status or report URL.

Risk: The reduction lane could be misused to hide plagiarism or evade academic-integrity rules.

Mitigation: Frame revision guidance around legitimate citation, independent analysis, and institutional disclosure rules; refuse tactics such as fake reports, hidden characters, or mechanical evasion.

Risk: Report verification may involve captchas, login, official page failures, or incomplete report identifiers.

Mitigation: Use official verification entries, have the user handle captchas or login steps, and say that authenticity cannot be determined automatically when required evidence is missing.

Risk: Temporary upload tickets, object-storage fields, or file contents could expose sensitive data if echoed in responses or logs.

Mitigation: Use temporary credentials only for the active request and redact upload URLs, tokens, object keys, authorization headers, full exception traces, and manuscript text from outputs.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/zslzxy/skills/paper-check)
- [Privacy and Safety](references/common/privacy-and-safety.md)
- [Safety and Commerce](references/safety-and-commerce.md)
- [Product Selection Playbook](references/common/product-selection-playbook.md)
- [Report Interpretation](references/common/report-interpretation.md)
- [Report Verification Tutorial](references/report-verify/tutorial.md)
- [REST Contract](references/rest-contract.md)
- [CQCCJY Report Verification Entry](https://vpcs.cqccjy.cn/pwp/verify)
- [Wanfang Report Verification](https://truth.wanfangdata.com.cn/)
- [CNKI Report Verification](https://check7.cnki.net/codeverify/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with JSON tool results and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include order numbers, status labels, character counts, next actions, and browser URLs returned by the configured services; temporary upload credentials and manuscript contents are not included.]

## Skill Version(s):

3.2.0 (source: server release evidence and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
