## Description: <br>
Check USCIS case status by receipt number using Selenium and undetected-chromedriver. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pkhanpara](https://clawhub.ai/user/pkhanpara) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to query USCIS case status from a receipt number and receive the latest case date and status message in a command-line workflow. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the receipt number supplied by the user to USCIS through browser automation. <br>
Mitigation: Use only receipt numbers you are authorized to check and avoid entering unrelated personal information. <br>
Risk: Frequent polling may trigger USCIS rate limits or cause long-running commands if the site is slow. <br>
Mitigation: Run checks sparingly and use a timeout when scripting the command. <br>
Risk: The install command uses an unpinned third-party Python package that automates Chromium. <br>
Mitigation: Review the package before installation and run it in an environment appropriate for browser automation. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pkhanpara/skills/uscis-case-status) <br>
- [Publisher profile](https://clawhub.ai/user/pkhanpara) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Guidance] <br>
**Output Format:** [Plain text command output with optional Markdown command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs case number, last update date, and status message; errors on invalid receipt numbers.] <br>

## Skill Version(s): <br>
1.0.0 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
