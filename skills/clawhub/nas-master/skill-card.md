## Description: <br>
A hardware-aware ASUSTOR NAS skill that helps index NAS file and system metadata through SMB crawling, SSH inspection, and Python/MySQL dashboard tooling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[afajohn](https://clawhub.ai/user/afajohn) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and NAS administrators use this skill to plan and generate read-only ASUSTOR NAS metadata indexing workflows, including Python scraping, SSH health checks, MySQL schema setup, and PHP/AJAX dashboard guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests NAS, SMB, and SSH access while indexing broad private file metadata and system state. <br>
Mitigation: Use dedicated read-only NAS and SSH accounts, restrict scans to approved volumes, and avoid hidden sensitive folders unless explicitly needed. <br>
Risk: SSH connections and system inspection can expose the environment to trust-on-first-use or credential handling mistakes. <br>
Mitigation: Pin or verify the SSH host key before connecting and store credentials outside shared artifacts or public repositories. <br>
Risk: The MySQL/PHP dashboard may expose indexed private file paths and NAS metadata. <br>
Mitigation: Secure or disable the dashboard, limit access to trusted users, and review indexed data before making it available. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/afajohn/skills/nas-master) <br>
- [Moltbot skills documentation](https://docs.molt.bot/tools/skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with Python, SQL, shell, and configuration snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate NAS indexing code, MySQL schema, environment configuration, and dashboard guidance; outputs should be reviewed before execution.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
