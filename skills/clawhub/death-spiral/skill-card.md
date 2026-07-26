## Description: <br>
Death Spiral helps agents diagnose self-reinforcing competitive decline by auditing moats, early-warning signals, cascade steps, and intervention windows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Strategy teams, founders, investors, and agents use this skill to evaluate whether market-share or growth decline is structural, map the competitive cascade, and identify an intervention window before the decline becomes self-reinforcing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Strategic or financial conclusions may be incorrect if based on stale, incomplete, or unverified company data. <br>
Mitigation: Verify market-share, CAC, churn, revenue, and R&D trend claims against current company data before acting on recommendations. <br>
Risk: The skill can misclassify cyclical decline as structural competitive decline. <br>
Mitigation: Apply the skill's fit checks and stop rule: test cyclicality, name specific moat-breach scenarios, and stop if the audit is incomplete. <br>


## Reference(s): <br>
- [Death Spiral on ClawHub](https://clawhub.ai/deciqai/skills/death-spiral) <br>
- [Sources - death-spiral](references/sources.md) <br>
- [Method in Action: Kodak's Death Spiral (1994-2012)](examples/kodaks-death-spiral-1994-2012.md) <br>
- [Competitive Advantage](https://www.simonandschuster.com/books/Competitive-Advantage/Michael-E-Porter/9780684841465) <br>
- [The Innovator's Dilemma](https://www.hbs.edu/faculty/Pages/item.aspx?num=46) <br>
- [Kodak SEC filings](https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0000031235) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with a structured Death Spiral Risk Map] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces analysis guidance only; verify strategic and financial claims with current company data before acting.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
