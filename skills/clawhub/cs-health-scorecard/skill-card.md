## Description: <br>
Builds a customer health scorecard for a specific account with RAG status, weighted dimension scores, key risks, renewal forecast, and recommended actions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Customer success teams and account leaders use this skill to assess account health, renewal risk, expansion potential, and next actions from recent account, product, support, engagement, and commercial data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The scorecard may process sensitive customer-success and commercial details. <br>
Mitigation: Use only account data you are authorized to process, and redact unnecessary personal or commercial details before sharing inputs or outputs. <br>
Risk: The skill text advertises a Python scoring helper, but the submitted package does not include that script. <br>
Mitigation: Verify weighted calculations manually or with an available trusted tool before relying on the headline score or RAG band. <br>
Risk: Scores and renewal forecasts can be misleading when based on stale data or unsupported judgment. <br>
Mitigation: Anchor each dimension score to recent named evidence and review the final scorecard before using it for account planning. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mohitagw15856/skills/cs-health-scorecard) <br>
- [Skill homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/cs-health-scorecard.html) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Guidance] <br>
**Output Format:** [Markdown scorecard with tables, weighted scores, RAG status, risks, renewal forecast, and action lists.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses a fixed customer-health rubric and weighted scoring framework; headline calculations should be checked because the advertised helper script is not included.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
