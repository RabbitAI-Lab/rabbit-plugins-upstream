## Description: <br>
HeartFlow is a local, rule-based text gate that helps agents check user input, drafts, and AI outputs for quality, reasoning, and safety signals before use. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mark-heartflow](https://clawhub.ai/user/mark-heartflow) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to add a local heuristic review layer around AI inputs, drafts, and outputs. It is best treated as a text quality and risk-screening aid, not as a verified fact checker or hardened security service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can be mistaken for a verified fact checker or hardened security control. <br>
Mitigation: Use it as a heuristic local text filter and review important decisions or claims through independent checks. <br>
Risk: Daemon or HTTP operation can expose a local service if enabled without review. <br>
Mitigation: Confirm the server code first, bind it to localhost, and restrict access before running any daemon or HTTP mode. <br>
Risk: Persistent error memory may store correction context under data/. <br>
Mitigation: Clear or disable error memory in shared, sensitive, or multi-user environments. <br>
Risk: Documentation and metadata may overstate or contradict the actual local rule-based behavior. <br>
Mitigation: Evaluate the skill on representative text before relying on its verdicts and document any observed limits for users. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mark-heartflow/skills/hf-pub) <br>
- [Publisher profile](https://clawhub.ai/user/mark-heartflow) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown, JavaScript examples, shell commands, and structured gate results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local rule-based checks can return pass, verify, rewrite, or block actions with supporting findings.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence; artifact package version 6.4.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
