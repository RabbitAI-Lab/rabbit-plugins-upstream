## Description: <br>
Checks an OATDA account's current balance, total usage, and remaining credits through the OATDA credits API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devcsde](https://clawhub.ai/user/devcsde) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, operators, and OATDA users use this skill to confirm available OATDA credits before expensive image, video, or long-running LLM calls. It helps agents present balance, spent amount, and top-up status without exposing the full API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires access to an OATDA API key for balance checks. <br>
Mitigation: Use it only with an intended OATDA account, store the key in OATDA_API_KEY or ~/.oatda/credentials.json, and do not print the full key in agent output. <br>
Risk: The balance response can influence whether an agent proceeds with expensive generation calls. <br>
Mitigation: Use actualBalance as the remaining-budget value and ask the user to top up or confirm before continuing when credits are low. <br>


## Reference(s): <br>
- [OATDA](https://oatda.com) <br>
- [OATDA credits API endpoint](https://oatda.com/api/v1/user/credits) <br>
- [OATDA credits dashboard](https://oatda.com/dashboard/credits) <br>
- [OATDA API keys dashboard](https://oatda.com/dashboard/api-keys) <br>
- [ClawHub skill page](https://clawhub.ai/devcsde/skills/oatda-check-balance) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration guidance, API calls] <br>
**Output Format:** [Markdown with shell commands and JSON response interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Reads OATDA_API_KEY from the environment or ~/.oatda/credentials.json and should not print the full key.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
