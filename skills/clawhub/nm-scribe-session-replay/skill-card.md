## Description: <br>
Converts a Claude Code session JSONL file into an animated GIF terminal replay. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and teams use this skill to turn selected Claude Code session JSONL files into shareable animated terminal GIFs for demos, pull request evidence, tutorials, and workflow highlights. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Generated replays may expose secrets, private paths, customer data, incident details, or proprietary prompts from selected session files. <br>
Mitigation: Use --turns and --show to limit included content, then review the generated replay before sharing it. <br>
Risk: The skill reads Claude Code session files and turns selected conversations into shareable GIFs. <br>
Mitigation: Install and run it only for sessions whose contents are appropriate for conversion and distribution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-session-replay) <br>
- [Publisher profile](https://clawhub.ai/user/athola) <br>
- [metadata.openclaw homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>
- [clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Shell commands, Configuration, Files, Guidance] <br>
**Output Format:** [Markdown/plain text status and guidance with generated VHS tape and GIF file paths.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May generate a temporary VHS tape and an animated GIF; output content depends on selected session turns and visibility filters.] <br>

## Skill Version(s): <br>
1.9.17 (source: release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
