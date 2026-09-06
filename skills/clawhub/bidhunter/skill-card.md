## Description:

BidHunter monitors Chinese state-owned enterprise and public procurement notices, compares notices against configurable qualification rules, generates bid-readiness reports, and can optionally use local document parsing plus MiniMax AI for tender review and risk analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[419597334-sudo](https://clawhub.ai/user/419597334-sudo)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, procurement operators, and bid teams use this skill to collect public tender notices, evaluate whether configured bidding entities appear qualified, prioritize opportunities, generate reports, and request AI-assisted tender summaries or risk checks when allowed.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sensitive bid documents or generated reports can be sent externally when optional MiniMax AI, webhook, email, DingTalk, or WeCom features are enabled.

Mitigation: Keep AI disabled unless document text is approved for MiniMax processing, and verify every webhook, email, and messaging destination before running the pipeline.

Risk: Untrusted source configuration or unnecessary local rule-editor exposure can affect collection and qualification behavior.

Mitigation: Use only trusted sources.json files and run the rule editor only while actively editing local rules.

Risk: Document parsing dependencies and AI summaries may produce incomplete or inaccurate tender extraction.

Mitigation: Pin or update parser dependencies, review parsed fields and AI recommendations manually, and treat bid advice as decision support rather than an authority.

## Reference(s):

- [BidHunter ClawHub skill page](https://clawhub.ai/419597334-sudo/skills/bidhunter)
- [Supported platforms and source configuration](references/platforms.md)
- [Filter rules and qualification logic](references/filter_rules.md)
- [Tender notice field schema](references/field_standard.md)
- [BidHunter setup guide](references/setup-guide.md)
- [BidHunter FAQ](scripts/docs/FAQ.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands, configuration snippets, text reports, JSONL data, and optional HTML reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May generate local report files, qualification JSONL outputs, calendar summaries, push notifications, webhook payloads, and AI-assisted tender summaries when optional services are configured.]

## Skill Version(s):

2.0.0 (source: SKILL.md frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
