## Description: <br>
Riveter (riveterhq.com) connector for searching and reading Riveter data through the OOMOL oo CLI instead of direct API calls. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to run read-oriented Riveter tasks through an OOMOL-connected account, including retrieving connected account and API-key details and scraping public webpages for extracted text. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The connector can retrieve Riveter account and API-key details for the connected account. <br>
Mitigation: Install and use the skill only when the user trusts OOMOL and intends to use the oo CLI with their Riveter account. <br>
Risk: The skill depends on live OOMOL authentication, a connected Riveter account, and available OOMOL billing credits. <br>
Mitigation: Run setup or billing steps only after an auth, connection, scope, credential, app readiness, or billing error occurs. <br>


## Reference(s): <br>
- [ClawHub Riveter Skill Page](https://clawhub.ai/oomol/skills/oo-riveter) <br>
- [Riveter Homepage](https://riveterhq.com) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include JSON responses from oo CLI connector actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: SKILL.md frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
