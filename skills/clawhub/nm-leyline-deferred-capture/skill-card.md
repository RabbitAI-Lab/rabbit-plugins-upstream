## Description: <br>
Defines the contract for deferred-item capture across plugins. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and plugin maintainers use this skill to design or validate deferred-capture wrappers that record deferred work through a consistent issue title, label taxonomy, body template, duplicate check, and dry-run JSON result. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A wrapper implementing this contract may create GitHub issues from supplied titles, context, labels, and artifact paths. <br>
Mitigation: Review the wrapper before use and exercise the dry-run compliance path before enabling issue creation. <br>
Risk: Deferred issue bodies may expose sensitive context or private artifact paths if those values are passed into the wrapper. <br>
Mitigation: Avoid passing secrets, private artifact paths, or sensitive project details in title, context, label, or artifact-path fields. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/athola/skills/nm-leyline-deferred-capture) <br>
- [Leyline Plugin Homepage](https://github.com/athola/claude-night-market/tree/master/plugins/leyline) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, JSON] <br>
**Output Format:** [Markdown guidance with CLI argument specifications, issue-template text, label taxonomy, shell-command examples, and JSON output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Defines a convention only; it does not include executable code or hidden behavior.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
