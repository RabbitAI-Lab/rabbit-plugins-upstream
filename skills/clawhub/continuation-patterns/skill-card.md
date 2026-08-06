## Description: <br>
Helps agents provide educational technical-analysis guidance on whether triangle, flag, pennant, wedge, rectangle, broadening, or diamond chart patterns indicate trend continuation or warn of reversal. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[bianchunhui](https://clawhub.ai/user/bianchunhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to interpret continuation chart patterns, distinguish them from reversal or support/resistance cases, and produce cautious educational market commentary. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Outputs may be mistaken for personalized financial advice. <br>
Mitigation: Present responses as educational technical-analysis commentary and avoid personalized trade recommendations. <br>
Risk: Continuation and reversal classifications can be wrong when trend stage is misread. <br>
Mitigation: Check trend stage and breakout confirmation, and route clear reversal or support/resistance prompts to the adjacent skills named in the artifact. <br>
Risk: Broad shape words may route a non-financial request to this skill. <br>
Mitigation: Confirm the user is asking about price-chart patterns before applying the methodology. <br>


## Reference(s): <br>
- [Server-resolved source provenance](https://github.com/bianchunhui/murphy-ta-skills/tree/main/continuation-patterns) <br>
- [ClawHub skill page](https://clawhub.ai/bianchunhui/skills/continuation-patterns) <br>
- [Artifact skill definition](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown guidance with structured reasoning steps] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Educational technical-analysis commentary; no code execution, data access, or persistence.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata and test-prompts.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
