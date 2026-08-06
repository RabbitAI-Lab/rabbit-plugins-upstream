## Description: <br>
Conducts fundamental and technical analysis of A-share stocks, including multi-factor stock selection, ratings, daily reports, and quantitative recommendations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[paudyyin](https://clawhub.ai/user/paudyyin) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and external users use this skill to run A-share market research workflows, generate daily market reports, and compare candidate stocks with technical, fundamental, fund-flow, chip, volume, and news factors. Outputs are informational and should not be treated as investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may write report and analysis outputs to fixed or local paths, including task logging to record.md. <br>
Mitigation: Run it only in the intended workspace and explicitly approve or disable record.md logging before use. <br>
Risk: Generated stock recommendations may be mistaken for investment advice. <br>
Mitigation: Treat reports and rankings as informational research aids and verify decisions with qualified financial review. <br>
Risk: Market-data dependencies can be unavailable, stale, or incomplete. <br>
Mitigation: Check the reported data date and validate important results against trusted market-data sources before relying on them. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/paudyyin/skills/stock-research) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or plain-text reports with JSON analysis artifacts and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces stock ratings, ranked recommendations, market summaries, and local report artifacts; recommendations are informational.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence and artifact version history) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
