## Description: <br>
Enables an agent to search and read Shopify REST Admin data through the OOMOL Shopify connector and oo CLI. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to let an assistant inspect Shopify REST Admin resources such as shops, blogs, pages, articles, and article tags through documented read-only actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill has a broad Shopify trigger and relies on third-party CLI setup. <br>
Mitigation: Install it only if you trust OOMOL, review CLI installation and authentication steps before running them, and keep use to the listed read-only actions. <br>
Risk: Shopify Admin reads may expose shop configuration or content data. <br>
Mitigation: Run actions only against the intended connected shop and do not treat the broad trigger as approval for write or destructive Shopify operations. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/oomol/skills/oo-shopify) <br>
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [Shopify REST Admin Homepage](https://www.shopify.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON payload examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Command results are JSON returned by the oo CLI for read-only Shopify REST Admin actions.] <br>

## Skill Version(s): <br>
1.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
