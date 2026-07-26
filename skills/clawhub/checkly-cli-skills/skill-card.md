## Description: <br>
Provides Checkly CLI command reference and Monitoring as Code workflows for creating, testing, deploying, importing, and troubleshooting synthetic monitors. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vince-winkintel](https://clawhub.ai/user/vince-winkintel) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and operators use this skill to guide Checkly CLI workflows for monitoring-as-code projects, including authentication, configuration, check creation, local testing, deployment, imports, account operations, and failure investigation. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can guide actions that change Checkly resources or account access, including deploy, destroy, import commit or cancel, check delete, and member update or delete commands. <br>
Mitigation: Review every sensitive command and require explicit user approval before execution; use dry-run or confirmation output where the Checkly CLI provides it. <br>
Risk: Checkly API keys, account IDs, and project secrets may be exposed if copied into files, logs, or shared transcripts. <br>
Mitigation: Keep credentials in environment variables or CI secret stores, and avoid committing or displaying secret values. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/vince-winkintel/skills/checkly-cli-skills) <br>
- [Checkly CLI Best Practices](artifact/references/best-practices.md) <br>
- [Checkly CLI Troubleshooting](artifact/references/troubleshooting.md) <br>
- [Checkly Documentation](https://www.checklyhq.com/docs/) <br>
- [Checkly Runtimes](https://www.checklyhq.com/docs/runtimes/) <br>
- [Playwright Documentation](https://playwright.dev/) <br>
- [Checkly CLI GitHub Issues](https://github.com/checkly/checkly-cli/issues) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline bash, TypeScript, JSON, and YAML snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes read-only investigation guidance and confirmation prompts for sensitive Checkly actions.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata and artifact/VERSION) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
