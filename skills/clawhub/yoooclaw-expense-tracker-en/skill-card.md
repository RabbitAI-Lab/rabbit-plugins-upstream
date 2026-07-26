## Description: <br>
Extracts personal expense transactions from mobile phone notifications, categorizes them by time and spending type, removes likely duplicates, and summarizes totals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vivalavida-say-hi](https://clawhub.ai/user/vivalavida-say-hi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Individual users use this skill to summarize spending from local phone notification records across date ranges and categories such as food delivery, shopping, transportation, utilities, transfers, refunds, and items needing confirmation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can read broad phone notification files containing bank, payment, merchant, transfer, contact, and other app notification contents. <br>
Mitigation: Install only when comfortable with that access, use narrow date ranges and categories, and review whether OpenClaw provides a confirmation opportunity before notification files are accessed. <br>
Risk: Broad activation triggers may cause the skill to run for general spending or bill questions and process more notification data than intended. <br>
Mitigation: Phrase prompts explicitly with the desired date range, category, and data path, and review the generated summary before relying on totals. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/vivalavida-say-hi/skills/yoooclaw-expense-tracker-en) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown spending summary with category totals, date totals, transaction details, transfers, refunds, and items to confirm] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read local notification JSON files for the requested date range and summarize sensitive financial and personal notification contents.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
