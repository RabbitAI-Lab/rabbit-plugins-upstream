## Description: <br>
Extracts hidden assumptions from a plan or document, prices the cost of being wrong against the cost to test, and produces a ranked assumption ledger, decisive tests, upgrade list, and honest confidence statement. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, product teams, and business reviewers use this skill before committing to a plan, PRD, model, forecast, or strategy so hidden assumptions are made explicit, ranked, and tested. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may process sensitive plans, forecasts, strategy documents, or spreadsheet assumptions. <br>
Mitigation: Only provide material the user is comfortable having an agent process, and remove confidential or regulated content when policy requires it. <br>
Risk: A ranked assumption ledger can mislead reviewers if entries are generic, untraceable, or based on incomplete source material. <br>
Mitigation: Require every ledger entry to trace to a quote, hardcoded value, or named omission in the supplied document before using it for decisions. <br>
Risk: Recommended tests may create false confidence if they only confirm an assumption or cost more than the downside they are testing. <br>
Mitigation: Keep only tests that can disprove the assumption, compare test cost against the cost of being wrong, and review the top assumptions before commitment. <br>


## Reference(s): <br>
- [Assumption Bounty ClawHub Page](https://clawhub.ai/mohitagw15856/skills/assumption-bounty) <br>
- [Assumption Bounty Homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/assumption-bounty.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with a ranked table, short action lists, and a confidence statement] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [No automatic execution, external tool use, credential access, or persistence is indicated by the artifact evidence.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
