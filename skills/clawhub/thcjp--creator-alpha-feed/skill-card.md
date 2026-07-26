## Description: <br>
Creator Alpha Feed collects AI-related posts from X, ranks them into KOL, tutorial or opinion, and industry tiers, sends a concise channel digest, and writes a full Obsidian Markdown report. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
AI content creators and teams use this skill to curate daily topic leads and industry updates from configured X accounts and keywords, then archive a ranked digest in Obsidian. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send selected X content summaries to a configured group channel, which may expose account-specific or non-public information visible in the active X session. <br>
Mitigation: Before running, confirm the whitelist accounts, keywords, webhook or chat destination, and that sharing the resulting digest with that channel is acceptable. <br>
Risk: The skill writes a full Markdown report to an Obsidian Vault, so an incorrect vault path or configuration can place the report in the wrong location. <br>
Mitigation: Confirm the Obsidian Vault path and collection configuration before installation or execution, and review the generated report location after a run. <br>


## Reference(s): <br>
- [Creator Alpha Feed on ClawHub](https://clawhub.ai/thcjp/skills/creator-alpha-feed) <br>
- [Skill homepage](https://skillhub.cn) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration guidance] <br>
**Output Format:** [Channel-ready text digest plus timestamped Obsidian Markdown report] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes ranked source summaries, links, collection status notes, and delivery warnings when a source cannot be collected.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
