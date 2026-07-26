## Description: <br>
Make AI-powered phone calls via Bland AI to book restaurants, make appointments, inquire about services, and report back with transcripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dru-ca](https://clawhub.ai/user/dru-ca) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to instruct an agent to place outbound phone calls through Bland AI, then retrieve call status, transcripts, summaries, and optional recording URLs. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can place real outbound phone calls that may create costs, contact third parties, or trigger consent obligations. <br>
Mitigation: Confirm the destination number, task, expected cost, jurisdiction, and recording setting before each call. <br>
Risk: Call transcripts, summaries, and optional recordings may contain private or regulated information processed by Bland AI. <br>
Mitigation: Avoid sensitive details unless Bland AI privacy, retention, and recording-consent requirements have been reviewed for the intended use. <br>
Risk: The skill requires a Bland AI API key that can authorize paid calls. <br>
Mitigation: Store the key in an environment variable or secret store, restrict access to it, and rotate it if exposed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/dru-ca/skills/phone-calls-bland) <br>
- [Bland AI app](https://app.bland.ai) <br>
- [Bland AI dashboard](https://app.bland.ai/dashboard) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires BLAND_API_KEY; can initiate outbound calls and return transcripts, summaries, status, and recording URLs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
