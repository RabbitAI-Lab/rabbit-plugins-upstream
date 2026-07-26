## Description: <br>
Automate George online banking (Erste Bank / Sparkasse Austria): login/logout, list accounts, and fetch transactions via Playwright. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[odrobnik](https://clawhub.ai/user/odrobnik) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technically capable banking users use this skill to automate George online banking workflows, including login/logout, account listing, portfolio lookup, transaction export, and optional data-carrier upload/signing. <br>

### Deployment Geography for Use: <br>
Austria <br>

## Known Risks and Mitigations: <br>
Risk: The skill can store reusable George session state and token material locally. <br>
Mitigation: Use it only on a trusted private machine, treat the workspace george directory and token.json as sensitive, and run logout after completing banking tasks. <br>
Risk: The data-carrier upload and signing commands can process payment or order files. <br>
Mitigation: Avoid datacarrier-upload and datacarrier-sign unless you explicitly intend to process those files, and verify any mobile-app approval prompt before confirming. <br>
Risk: Account, transaction, portfolio, export, and debug outputs can contain sensitive banking information. <br>
Mitigation: Keep generated files private, avoid sharing debug outputs, and remove temporary banking artifacts when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/odrobnik/skills/george) <br>
- [Setup](SETUP.md) <br>
- [Unified Banking Schema](docs/unified-banking-schema.md) <br>
- [Skill homepage](https://github.com/odrobnik/george-skill) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, JSON, Files] <br>
**Output Format:** [Markdown guidance with shell commands; runtime commands can produce JSON, CSV, PDF, and text output.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Outputs can contain sensitive banking data and may include account, transaction, portfolio, export, upload, signing, or debug artifacts.] <br>

## Skill Version(s): <br>
1.5.5 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
