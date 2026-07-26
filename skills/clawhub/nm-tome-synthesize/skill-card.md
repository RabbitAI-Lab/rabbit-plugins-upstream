## Description: <br>
Merges, dedupes, ranks, and formats research findings into a report after research agents return results from multiple channels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and research teams use this skill to merge, deduplicate, rank, group, and format findings from multiple research-agent channels into a final report. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad activation triggers such as format or report could activate the skill outside an intended research-synthesis context. <br>
Mitigation: Use the skill explicitly after research agents have returned findings and verify that a research synthesis task is intended. <br>
Risk: A synthesized report can make incomplete or inaccurate source findings appear ranked and final. <br>
Mitigation: Review the source findings and final report before relying on the synthesis for decisions or publication. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-tome-synthesize) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/tome) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown report, brief, or transcript] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces ranked research synthesis from prior research findings; no bundled code, persistence, credential access, or exfiltration behavior is indicated by the security evidence.] <br>

## Skill Version(s): <br>
1.9.16 (source: release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
