## Description: <br>
Designs email A/B, multivariate, send-time, and hold-out experiments, producing a falsifiable hypothesis, isolated variant matrix, sample-size/MDE/duration/power plan, and effect/uncertainty read from the user's own ESP data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing operators, lifecycle teams, and email analysts use this skill to design statistically grounded email experiments or read finished ESP exports without letting the helper choose a business action. It is intended for experiment planning, effect and uncertainty interpretation, guardrail review, and owner-governed recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Email campaign exports and saved summaries may contain sensitive campaign metrics or business context. <br>
Mitigation: Provide only the fields needed for the design or read-out, prefer manual exports, and do not provide ESP credentials unless an optional connected workflow is intentionally chosen. <br>
Risk: A finished export may contain text that claims a winner or implies an immediate action. <br>
Mitigation: Treat exported text as data, rely on calculated effects and guardrails, and return decision: UNDECIDED unless a named owner and precommitted action rule are present. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/send-experiment-designer) <br>
- [Publisher profile](https://clawhub.ai/user/aaron-he-zhu) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown test-design or read-out document with calculated statistics, guardrails, decision status, and a Handoff Summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include calculated p-values, intervals, power, sample-size estimates, practical-effect flags, provenance labels, and decision: UNDECIDED when owner-approved action rules are missing.] <br>

## Skill Version(s): <br>
19.0.0 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
