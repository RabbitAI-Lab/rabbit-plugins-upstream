## Description: <br>
Creator Alpha Feed Free helps AI content creators collect AI-related X feed content, rank useful items, and write a daily Markdown report into an Obsidian vault. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Personal AI content creators use this skill to gather recent AI-related X posts from a home feed, whitelist accounts, and keyword searches, then generate ranked daily topic material in Obsidian. It is suited to recurring content discovery and lightweight archiving workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may operate through a logged-in X browser session and collect feed-derived content into local reports. <br>
Mitigation: Run it only with a browser session and feed sources you trust, and review collected content and links before relying on the report. <br>
Risk: The skill writes generated reports to a local Obsidian vault path. <br>
Mitigation: Use only a vault path you are comfortable writing to, confirm the configured directory before execution, and keep backups for important notes. <br>
Risk: Providing callback_url can send completion information to an external endpoint. <br>
Mitigation: Leave callback_url unset unless you fully trust and control the destination endpoint. <br>


## Reference(s): <br>
- [Skill homepage](https://skillhub.cn) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/creator-alpha-feed-free) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, configuration guidance] <br>
**Output Format:** [Markdown report with status text, summaries, ranked links, and execution notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes timestamped reports to an Obsidian vault path when configured; may also return failure codes and diagnostic messages.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
