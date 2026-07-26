## Description: <br>
Tax Professional helps users assess U.S. tax deductions, track deductible expenses, plan estimated payments, review audit risk, and prepare year-end tax summaries across W-2, 1099, S-Corp, and mixed employment situations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scottfo](https://clawhub.ai/user/scottfo) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Individuals, contractors, and small business owners with U.S. tax needs use this skill to evaluate deductions, log tax-relevant expenses, plan quarterly payments, and prepare year-end summaries. Users should verify material tax decisions against current IRS guidance or a qualified tax professional. <br>

### Deployment Geography for Use: <br>
United States <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read personal tax profile context and store tax or expense records in the workspace. <br>
Mitigation: Use it only with consent for that data handling, avoid entering unnecessary sensitive details, and protect or remove generated data files according to the user's retention needs. <br>
Risk: Tax guidance can become outdated or may not fit the user's full filing situation. <br>
Mitigation: Verify important decisions with current IRS guidance or a qualified tax professional before relying on the recommendation. <br>
Risk: The artifact includes commands that can create persistent Telegram tax reminders. <br>
Mitigation: Run reminder setup commands only after explicit user approval, and review the schedule, message content, and Telegram channel before enabling them. <br>
Risk: The skill references other skills' financial and vehicle data paths. <br>
Mitigation: Review which local data files are consulted before cross-skill use and limit access to records needed for the tax task. <br>


## Reference(s): <br>
- [Tax Professional ClawHub listing](https://clawhub.ai/scottfo/skills/tax-professional) <br>
- [Publisher profile](https://clawhub.ai/user/scottfo) <br>
- [Skill homepage](https://github.com/ScotTFO/tax-professional-skill) <br>
- [IRS](https://www.irs.gov) <br>
- [Common Write-Offs People Miss](references/common-writeoffs.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text guidance, Markdown, JSON data files, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with JSON expense records and optional shell command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read user tax context and write tax profile, expense, estimated payment, and return-analysis files under data/tax-professional/.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
