## Description: <br>
Use chill.institute in a browser to search for user-selected content and send the selected result to put.io. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baanish](https://clawhub.ai/user/baanish) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Users with chill.institute and put.io accounts use this skill to have an agent navigate the web UI, search for an item, start a put.io transfer, and optionally verify the transfer with the putio skill. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The workflow can act inside a logged-in chill.institute or put.io browser session. <br>
Mitigation: Complete OAuth directly, do not share passwords in chat, and ask the agent to show the selected result before starting a transfer. <br>
Risk: The optional verification step depends on a separate putio skill. <br>
Mitigation: Run the verification command only when that separate skill is installed and trusted. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/baanish/skills/chill-institute) <br>
- [chill.institute sign-in](https://chill.institute/sign-in) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands] <br>
**Output Format:** [Markdown instructions with an optional shell command] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses an interactive browser session and may rely on a separate putio skill for transfer verification.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
