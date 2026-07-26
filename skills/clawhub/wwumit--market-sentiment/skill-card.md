## Description: <br>
Analyzes user-provided CSV market data with a four-dimension sentiment model to produce a 0-100 market score, market state, and planning guidance. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wwumit](https://clawhub.ai/user/wwumit) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and financial researchers use this skill to summarize market sentiment from CSV inputs and translate the result into a market-state parameter for planning workflows. Its outputs are advisory context only and are not investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Financial sentiment output could be mistaken for trading advice. <br>
Mitigation: Present the output as advisory context only and require users to make independent investment decisions using their own risk tolerance and professional advice. <br>
Risk: Incorrect, incomplete, delayed, or mismapped CSV data can produce misleading scores and market states. <br>
Mitigation: Validate CSV source quality, required columns, and date coverage before using the results in planning workflows. <br>
Risk: The emitted stock-planner market parameter may not match a user's downstream workflow semantics. <br>
Mitigation: Verify the market parameter mapping against the target stock-planner workflow before relying on it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/wwumit/skills/market-sentiment) <br>
- [Artifact README](artifact/README.md) <br>
- [Artifact SKILL.md](artifact/SKILL.md) <br>
- [Artifact changelog](artifact/CHANGELOG.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown-style text reports, JSON objects, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads user-provided CSV market data and emits a score, market state, stock-planner market parameter, suggested position guidance, and threshold guidance.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata, package.json, CHANGELOG) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
