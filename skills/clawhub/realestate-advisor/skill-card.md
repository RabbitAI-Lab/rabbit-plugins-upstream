## Description: <br>
Realestate Advisor helps property owners, buyers, and home switchers understand residential property value, comparable transactions, listing competition, market posture, affordability, offer strategy, and replacement timing using public market data and transparent confidence levels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[perrykono-debug](https://clawhub.ai/user/perrykono-debug) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users use this skill to evaluate residential real-estate decisions, including owner valuation checks, buyer property assessment, offer strategy, and sell-then-buy versus buy-then-sell planning. It is intended as market-reference analysis, not an official appraisal, legal advice, or investment recommendation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Scheduled heartbeat maintenance may modify or delete workspace memory or archive files without clear user control. <br>
Mitigation: Review HEARTBEAT.md before installation and disable or edit its scheduled cleanup tasks if automatic memory or archive changes are not desired. <br>
Risk: Real-estate screenshots or chat excerpts may contain personal data or exact property identifiers. <br>
Mitigation: Redact names, phone numbers, unit numbers, account identifiers, chats, QR codes, and other sensitive details before sharing inputs with the skill. <br>
Risk: Market estimates and decision signals can be misleading if public transaction or listing data is stale, sparse, or incomplete. <br>
Mitigation: Treat outputs as market-reference analysis only, check cited data freshness and confidence, and use qualified professionals for official appraisal, legal, tax, or investment decisions. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown with structured sections and confidence labels] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include comparable transaction summaries, listing competition analysis, market-state labels, decision signals, affordability estimates, offer ranges, and viewing checklists.] <br>

## Skill Version(s): <br>
2.0.3 (source: server release metadata; artifact text references v2.0.2) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
