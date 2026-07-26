## Description: <br>
Fast Apple Mail search via SQLite on macOS. Search emails by subject, sender, date, attachments - results in ~50ms vs 8+ minutes with AppleScript. Use when asked to find, search, or list emails. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mneves75](https://clawhub.ai/user/mneves75) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and macOS users use this skill to search Apple Mail metadata quickly from a local command-line workflow, including subject, sender, date, unread, attachment, and export-oriented queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Search results and JSON/CSV exports may contain private email metadata. <br>
Mitigation: Keep searches narrow and review exported results before sharing or storing them outside the local machine. <br>
Risk: Installing an unverified mail-search executable into /usr/local/bin could expose local mail metadata to an untrusted command. <br>
Mitigation: Verify the separate mail-search executable before installing or running it. <br>


## Reference(s): <br>
- [ClawHub Apple Mail Search page](https://clawhub.ai/mneves75/skills/apple-mail-search) <br>


## Skill Output: <br>
**Output Type(s):** [text, JSON, CSV, shell commands, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and optional text, JSON, or CSV command output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally on macOS and requires sqlite3; searches are read-only and limited to Apple Mail metadata.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
