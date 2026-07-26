## Description: <br>
Perigon (perigon.io) lets an agent search, read, and summarize Perigon data through the OOMOL oo CLI connector. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users use this skill to query Perigon news, entities, sources, stories, topics, and Wikipedia-backed data through an OOMOL-connected Perigon account. It also supports AI summaries and semantic search over Perigon news and Wikipedia content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may require installing the OOMOL oo CLI with shell or PowerShell installer commands. <br>
Mitigation: Review the installer source and install only from trusted OOMOL CLI sources before running connector actions. <br>
Risk: Connector actions use the user's OOMOL-connected Perigon account and may fail or expose account-scoped data if the wrong connection or payload is used. <br>
Mitigation: Confirm the Perigon connection and inspect the live action schema before sending JSON payloads. <br>
Risk: Generated news summaries and search results may be incomplete or dependent on Perigon coverage and filters. <br>
Mitigation: Review returned articles, filters, and source metadata before using summaries for decisions. <br>


## Reference(s): <br>
- [ClawHub Perigon skill](https://clawhub.ai/oomol/skills/oo-perigon) <br>
- [OOMOL publisher profile](https://clawhub.ai/user/oomol) <br>
- [Perigon homepage](https://perigon.io) <br>
- [oo CLI](https://github.com/oomol-lab/oo-cli) <br>
- [OOMOL Perigon connection](https://console.oomol.com/app-connections?provider=perigon) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The skill instructs the agent to inspect the live connector schema before building an oo CLI JSON payload.] <br>

## Skill Version(s): <br>
1.0.1 (source: server evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
