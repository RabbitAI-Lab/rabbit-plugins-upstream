## Description: <br>
ScrapeGraphAI helps agents search, scrape, and extract structured data through an OOMOL-connected ScrapeGraphAI account. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[oomol](https://clawhub.ai/user/oomol) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to run ScrapeGraphAI extraction, scraping, search, quota, and history actions through the oo CLI after connecting their OOMOL account. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Searches, scraping targets, prompts, and extraction inputs may be sent to the connector service. <br>
Mitigation: Avoid submitting sensitive private pages or data unless that transfer is intended and authorized. <br>
Risk: The skill depends on a signed-in OOMOL account, a connected ScrapeGraphAI app, and available billing credits. <br>
Mitigation: Run setup or billing steps only after the corresponding auth, connection, or credit error appears. <br>


## Reference(s): <br>
- [ClawHub ScrapeGraphAI Skill](https://clawhub.ai/oomol/skills/oo-scrape-graph-ai) <br>
- [ScrapeGraphAI Homepage](https://scrapegraphai.com) <br>
- [oo CLI Repository](https://github.com/oomol-lab/oo-cli) <br>
- [oo CLI Install Guide](https://cli.oomol.com/install-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration instructions, JSON] <br>
**Output Format:** [Markdown with inline shell commands and JSON payload guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Connector command responses are expected as JSON containing data and meta.executionId.] <br>

## Skill Version(s): <br>
1.0.0 (source: release evidence and SKILL.md metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
