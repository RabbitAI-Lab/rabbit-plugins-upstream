## Description: <br>
Find official, trusted, vendor-owned AI agent skills from Skillscout. Use when a user asks what skills exist for a company/product/domain, asks for official skills, trusted skills, vendor skills, or install commands for agent skills from official sources. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ulyanas](https://clawhub.ai/user/ulyanas) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agent users use this skill to find official Skillscout listings for a company, product, domain, or vendor and return install commands, source links, and concise catalog summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can make network requests to Skillscout for current catalog data or read a configured local catalog JSON file. <br>
Mitigation: Use the official Skillscout source or a trusted local data file, and review listed skills before running install commands. <br>
Risk: Catalog results may be stale or incomplete when a local data source is used. <br>
Mitigation: Use the remote Skillscout directory when current production data matters and include source links so users can inspect listed skills. <br>


## Reference(s): <br>
- [Server-resolved source](https://github.com/ulyanas/skillscout-skills/tree/main/skills/find-official-skills) <br>
- [ClawHub skill page](https://clawhub.ai/ulyanas/skills/find-official-skills) <br>
- [Skillscout official skills directory](https://skillscout.sh/data/official-skills-universal.json) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown or plain text with inline shell commands and links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include machine-readable JSON from the bundled search script when the user asks for exports.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
