## Description: <br>
Queries the JFTech Open Platform for device lists bound to a developer account, with pagination and optional serial-number filtering. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jftech](https://clawhub.ai/user/jftech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External developers and device operations teams use this skill to query JFTech devices bound to an open-platform account, either by page or by a list of device serial numbers. <br>

### Deployment Geography for Use: <br>
China mainland, Asia, Europe, and North America, based on the documented JFTech API endpoint regions. <br>

## Known Risks and Mitigations: <br>
Risk: Device passwords, login tokens, and account credentials can be exposed in command output, JSON output, logs, tickets, or chat transcripts. <br>
Mitigation: Use only in a trusted workspace, avoid JSON output unless raw records are intentionally needed, and redact passwords and login tokens before sharing results downstream. <br>
Risk: The skill makes authenticated requests to region-specific JFTech API endpoints and can enumerate devices bound to the configured account. <br>
Mitigation: Run it only with authorized JFTech credentials, verify the selected JF_ENDPOINT region before use, and limit serial-number queries to intended devices. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/jftech/skills/jf-open-pro-device-list) <br>
- [JFTech Open Platform documentation](https://docs.jftech.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, shell commands, guidance] <br>
**Output Format:** [Plain text tables or simple text, with optional JSON device records] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can include device serial numbers, usernames, nicknames, passwords, and login tokens returned by the JFTech API.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata; artifact frontmatter says 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
