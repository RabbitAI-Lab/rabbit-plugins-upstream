## Description: <br>
Smartlead helps agents search and read Smartlead campaign, lead, and email-account data through an OOMOL-connected Smartlead account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers with a connected Smartlead account use this skill to inspect campaigns, campaign leads, and email accounts without calling the Smartlead API directly. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Read-only Smartlead actions can expose campaign, lead, and email-account data from the connected account. <br>
Mitigation: Review command output before sharing it outside the authorized workflow. <br>
Risk: The skill depends on trust in OOMOL and a connected Smartlead account. <br>
Mitigation: Install only when the user trusts OOMOL and is comfortable connecting Smartlead to the OOMOL connector. <br>


## Reference(s): <br>
- [ClawHub Smartlead skill](https://clawhub.ai/oomol/skills/oo-smartlead-ai) <br>
- [Smartlead homepage](https://www.smartlead.ai) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only Smartlead campaign, lead, and email-account data may be returned from the connected account.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
