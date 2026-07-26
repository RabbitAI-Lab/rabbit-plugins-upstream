## Description: <br>
Query configured MySQL databases with automatic SSH tunnel setup, teardown, and SQL execution. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[zenixp](https://clawhub.ai/user/zenixp) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and operators use this skill to list configured databases and run SQL queries against local or SSH-tunneled MySQL databases. It is most useful when an agent needs controlled access to project databases through a shared configuration file. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can give an agent broad access to configured production databases. <br>
Mitigation: Use least-privilege database accounts, preferably read-only by default, and keep production and test database names unambiguous. <br>
Risk: Destructive or privilege-changing SQL can modify data or permissions. <br>
Mitigation: Review UPDATE, DELETE, DROP, ALTER, INSERT, and privilege-changing queries before execution. <br>
Risk: Database and SSH credentials can be exposed if stored carelessly. <br>
Mitigation: Prefer environment variables for database and SSH passwords, and avoid storing sensitive credentials in shared configuration files. <br>
Risk: SSH tunnel configuration can expose sensitive hosts or trust unexpected host keys. <br>
Mitigation: Prefer SSH keys and pinned host keys for sensitive hosts, and review tunnel destinations before use. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/zenixp/skills/db-query) <br>
- [Installation guide](scripts/INSTALL.md) <br>
- [Example database configuration](scripts/config.example.json) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and command-line query output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May print database rows, status messages, and error text from the MySQL and SSH clients.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
