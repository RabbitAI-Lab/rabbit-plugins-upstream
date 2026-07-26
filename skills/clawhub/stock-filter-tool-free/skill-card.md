## Description: <br>
This skill helps agents screen A-share stocks using fundamental and technical criteria such as PE, PB, ROE, moving averages, and RSI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and personal investors use this skill to perform preliminary A-share stock screening with basic fundamental, technical, industry, and market-cap filters. Results should be treated as analysis support, not investment advice. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security summary flags broad activation language plus command and write authority. <br>
Mitigation: Review prompts and generated commands before execution, and run the skill with only the file and command permissions required for the stock-screening task. <br>
Risk: The security guidance warns that callback_url can send results to an external destination. <br>
Mitigation: Use callback_url only with destinations the user trusts and avoid sending sensitive portfolio or screening data to unverified endpoints. <br>
Risk: The security guidance says export support is undefined for the free edition. <br>
Mitigation: Treat export behavior as unsupported until the publisher clarifies the free-edition capability matrix. <br>
Risk: The artifact describes delayed public market data and notes that screening results are for reference only. <br>
Mitigation: Validate screened securities with current market data and independent analysis before making investment decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/stock-filter-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, Text] <br>
**Output Format:** [Markdown with inline shell commands and structured examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include stock-screening conditions, command examples, status text, result summaries, and logs.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
