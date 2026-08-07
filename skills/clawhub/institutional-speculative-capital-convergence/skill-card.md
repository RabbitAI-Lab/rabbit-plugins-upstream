## Description: <br>
牛股王机游共振 helps agents screen A-share stocks using institutional-capital and speculative-capital signals, with strategy views for trend leaders, swing opportunities, and small-cap growth candidates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[maomaoxx779-cmd](https://clawhub.ai/user/maomaoxx779-cmd) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to query and summarize A-share stock pools selected by 牛股王's institutional and speculative capital convergence model. It supports current and historical stock-pool checks, strategy comparison, institutional attention ranking, and industry concentration review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan reports a hardcoded usertoken in the skill text. <br>
Mitigation: Review before installation, remove or replace the token, rotate it if it is real, and avoid reusing it in downstream integrations. <br>
Risk: The skill produces stock-screening output that users could mistake for investment advice. <br>
Mitigation: Verify the data source, preserve the investment disclaimer, and require human review before making trading decisions. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/maomaoxx779-cmd/skills/institutional-speculative-capital-convergence) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/maomaoxx779-cmd) <br>
- [牛股王 app and PC download page](https://www.stockhn.com/#/appDownload) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown text with optional curl examples, tables, and required source and AI disclaimer notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Responses are expected to identify the 牛股王 data source and include an investment-advice disclaimer.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence and artifact manifest) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
