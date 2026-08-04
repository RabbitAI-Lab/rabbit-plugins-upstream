## Description: <br>
Check USCIS case status by receipt number. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pkhanpara](https://clawhub.ai/user/pkhanpara) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to check USCIS case status for a provided receipt number and receive the case number, last update date, and status message. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The provided USCIS receipt number is submitted to the USCIS website through browser automation. <br>
Mitigation: Use the skill only when sharing the receipt number with USCIS for a case-status lookup is acceptable. <br>
Risk: Frequent polling may trigger USCIS rate limits or cause lookups to fail. <br>
Mitigation: Avoid polling faster than once every few minutes and add timeouts when scripting repeated checks. <br>
Risk: USCIS outages or slow responses may cause the command to hang. <br>
Mitigation: Run the command with a timeout, such as a 60 to 90 second limit, in automation. <br>
Risk: The skill relies on third-party browser automation and a local Chromium browser setup. <br>
Mitigation: Install only in environments where Selenium, undetected-chromedriver, Xvfb, and Chromium are acceptable operational dependencies. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pkhanpara/skills/uscis-case-status) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, guidance] <br>
**Output Format:** [Plain text command output with markdown usage guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs receipt number, last update date, and status message when the USCIS lookup succeeds.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
