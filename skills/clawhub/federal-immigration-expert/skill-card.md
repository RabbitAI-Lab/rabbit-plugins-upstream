## Description:

Generic Canadian federal immigration policy expert (IRCC Express Entry / CRS / CEC / FSW / FST). Fetches policy in real time from official sources, detects and surfaces updates, and computes multi-stream eligibility plus CRS scoring (with itemized detail) for any candidate. All policy judgements follow live official sources, never stale offline data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[forrest-tech](https://clawhub.ai/user/forrest-tech)

### License/Terms of Use:

MIT

## Use Case:

External users and agents use this skill to estimate Canadian federal Express Entry eligibility, CRS score, and practical improvement actions for candidate profiles. Results should be treated as immigration planning support and verified against IRCC before action.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Users may treat offline estimates or monitored policy changes as live IRCC or legal advice.

Mitigation: Verify eligibility, CRS scores, draws, and program rules directly with IRCC before making immigration decisions.

Risk: Scheduled monitoring and source discovery can make network requests beyond a local scoring workflow.

Mitigation: Review or disable cron, policy_monitor.py, and auto_discover.py if only local scoring or federal canada.ca sources are acceptable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/forrest-tech/skills/federal-immigration-expert)
- [IRCC Express Entry draw history](https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations.html)
- [IRCC category-based selection](https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/submit-profile/rounds-invitations/category-based-selection.html)
- [IRCC Canadian Experience Class eligibility](https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/who-can-apply/canadian-experience-class.html)
- [IRCC Federal Skilled Worker eligibility](https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/who-can-apply/federal-skilled-workers.html)
- [IRCC Federal Skilled Trades eligibility](https://www.canada.ca/en/immigration-refugees-citizenship/services/immigrate-canada/express-entry/who-can-apply/federal-skilled-trades.html)
- [Official IRCC source manifest](data/sources.json)
- [CEC official snapshot](data/snapshots/ircc-cec-OFFICIAL.txt)
- [FSW official snapshot](data/snapshots/ircc-fsw-OFFICIAL.txt)
- [FST official snapshot](data/snapshots/ircc-fst-OFFICIAL.txt)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, guidance]

**Output Format:** [Markdown reports with eligibility tables, scoring details, action guidance, and optional JSON-driven script output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May use candidate profile JSON passed to the evaluator script; no API key is required for local scoring.]

## Skill Version(s):

1.2.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
