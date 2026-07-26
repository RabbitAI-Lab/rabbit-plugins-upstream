## Description: <br>
CLI für den Zugriff auf das österreichische Firmenbuch (HVD WebServices). <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pasogott](https://clawhub.ai/user/pasogott) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agents use this skill to install and operate the firmenbuchat CLI for Austrian company register lookup, company and document searches, document downloads, and change queries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing from a third-party GitHub or Homebrew source can introduce supply-chain risk. <br>
Mitigation: Install only when the publisher and source are trusted, and review the release before deployment. <br>
Risk: The FIRMENBUCH_API_KEY credential can be exposed if passed directly on the command line or committed in a local environment file. <br>
Mitigation: Prefer the tool's config flow or a protected .env file, avoid command-line secrets, and keep local secret files out of repositories. <br>
Risk: Large document-change query windows may fail with server errors. <br>
Mitigation: Use smaller date ranges for large change queries. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/pasogott/skills/firmenbuchat) <br>
- [Project homepage](https://github.com/pasogott/firmenbuch-aip) <br>
- [UV install source](https://github.com/pasogott/firmenbuch-aip.git) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline shell commands and CLI examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce or describe table, JSON, or raw CLI output depending on the firmenbuchat command options.] <br>

## Skill Version(s): <br>
0.2.3 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
