## Description: <br>
Creates paid Life Book full-report Agent tasks, checks async status, and retrieves the generated 18-chapter report through the official Agent API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xcii](https://clawhub.ai/user/0xcii) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agent operators use this skill to collect Life Book intake data, create paid full-report tasks, handle payment states, poll async status, and retrieve completed reports. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends birth data, life history, questions, payment status, and generated reports to a configured Life Book API. <br>
Mitigation: Confirm the configured service is trusted and that its privacy, retention, deletion, and operator-access terms are acceptable before submitting sensitive details. <br>
Risk: Payment or report readiness could be misrepresented if an agent relies on user statements instead of the official API state. <br>
Mitigation: Treat official API responses as authoritative and do not claim payment success, x402 verification, generation start, or report readiness unless returned by the API. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/0xcii/skills/life-book-generator) <br>
- [Life Book service](https://www.elife369.site) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include task IDs, one-time task tokens, payment details, status URLs, and generated report content when the official API returns them.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and package.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
