## Description: <br>
Group related tickers into named investment themes with AI-generated summaries and news keyword monitoring. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent developers use this skill to create, inspect, update, and delete saved AlphaGBM investment-theme baskets, then present theme summaries, ticker movement, and matched news in a concise research view. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses an AlphaGBM API key to read and manage saved investment themes. <br>
Mitigation: Install only when the agent is intended to access AlphaGBM theme data, and keep API-key use limited to the documented service calls. <br>
Risk: Create, update, and delete requests can change stored theme baskets. <br>
Mitigation: Confirm mutating requests with the user before execution, especially hard-delete actions. <br>
Risk: Broad finance terms such as theme or basket may activate the skill during adjacent investment conversations. <br>
Mitigation: Check that the user is asking about AlphaGBM theme management before using the skill. <br>


## Reference(s): <br>
- [AlphaGBM](https://alphagbm.com) <br>
- [ClawHub skill page](https://clawhub.ai/clementgu/skills/alphagbm-theme-research) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown summaries, tables, and concise confirmations based on AlphaGBM API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include theme summaries, ticker grids, matched news, and create/update/delete confirmations.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
