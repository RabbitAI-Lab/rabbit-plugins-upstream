## Description: <br>
Merges, dedupes, ranks, and formats research findings into a report for use after research agents return results from multiple channels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, researchers, and research agents use this skill after multi-channel research to merge, dedupe, rank, group by theme, and format findings into a final report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad trigger words such as merge, rank, format, and report could activate the skill unintentionally. <br>
Mitigation: Invoke the skill explicitly or rename triggers in environments that automatically route generic commands. <br>
Risk: Using the skill without an active research session can produce an incomplete or context-poor report. <br>
Mitigation: Run it only after research agents have returned findings from the relevant channels. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-tome-synthesize) <br>
- [Tome plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/tome) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown report, brief, or transcript] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can produce a full sectioned report, a condensed 1-2 page brief, or a raw session log.] <br>

## Skill Version(s): <br>
1.9.17 (source: release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
