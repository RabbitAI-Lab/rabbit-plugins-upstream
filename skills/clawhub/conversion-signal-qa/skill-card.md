## Description: <br>
Conversion Signal Qa helps agents QA paid-ad conversion tracking before launch by checking conversion-event firing, UTM hygiene, cross-platform deduplication rules, attribution-window alignment, and offline or iOS-ATT modeled-gap flags. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators, growth teams, and developers use this skill before launching or scaling paid campaigns to verify conversion tracking, UTMs, deduplication, attribution windows, and modeled or offline tracking gaps. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses user-provided GA4, ecommerce, and manual test conversion evidence that may contain sensitive business or customer-adjacent data. <br>
Mitigation: Provide only the necessary own-data exports and remove unrelated sensitive fields before sharing them with an agent. <br>
Risk: The skill may persist tracking specs, reports, and unresolved signal issues for future sessions when the user approves memory writes. <br>
Mitigation: Review the proposed saved content and approve memory writes only when the retained tracking details are appropriate to keep. <br>
Risk: UTM values can accidentally include personal data such as names, emails, or order identifiers. <br>
Mitigation: Use the UTM/event spec rule that forbids PII in UTM fields and keep order identifiers in conversion deduplication parameters instead. <br>


## Reference(s): <br>
- [Tracking Pre-Flight Checklist](artifact/references/preflight-checklist.md) <br>
- [UTM / Event Spec Builder](artifact/references/utm-event-spec.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/conversion-signal-qa) <br>
- [Metadata Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown pre-flight report with checklist results, UTM naming convention, conversion-event spec table, deduplication notes, attribution-window notes, gap flags, and handoff summary.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May save the report and reusable UTM/event spec only after the user approves memory writes.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release evidence and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
