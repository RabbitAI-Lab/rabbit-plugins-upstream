## Description: <br>
HeartFlow is a local, rule-based text discrimination engine that checks AI input, drafts, and output for safety, reasoning, confidence, and manipulation signals without an LLM dependency. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mark-heartflow](https://clawhub.ai/user/mark-heartflow) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent builders use this skill to run local rule-based checks on user input, draft responses, and final AI output. It returns pass, verify, rewrite, or block decisions with findings and rewrite guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may retain correction snippets and generated rules in local JSON files when its memory APIs are used. <br>
Mitigation: Review memory use before deployment, avoid storing sensitive user content, and clear local memory files according to policy. <br>
Risk: Rule-based checks are not a strict safety boundary or complete production moderation system. <br>
Mitigation: Use the skill as a supplemental validation layer with additional review or dedicated safety controls for high-risk deployments. <br>
Risk: Package metadata includes broader workflow labels than the shipped artifact appears to implement. <br>
Mitigation: Review exposed APIs and shipped files before relying on advertised workflows or integrating optional capabilities. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mark-heartflow/skills/heartflow) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Code, Configuration, Guidance] <br>
**Output Format:** [JSON-like JavaScript objects and concise guidance strings] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Local rule-based checks with no LLM dependency; optional memory APIs can write local JSON files.] <br>

## Skill Version(s): <br>
6.4.1 (source: frontmatter, package.json, VERSION, server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
