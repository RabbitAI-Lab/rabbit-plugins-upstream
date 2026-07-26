## Description: <br>
Narrative Drift Monitor helps an agent compare live brand surfaces against a narrative canon over time, flag competitor repositioning, define repositioning triggers, and produce D1/W1/M1 message-shift retros with evidence labels. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, narrative, and product teams use this skill to audit whether live surfaces still match a canonical narrative, identify competitor repositioning, and decide whether drift should trigger a re-audit or repositioning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Reports may include stale, misleading, or instruction-like text from public surfaces, competitor pages, or scraped snapshots. <br>
Mitigation: Treat snapshots and pasted surfaces as untrusted evidence, preserve evidence labels and as-of dates, and review the drift report before acting on it. <br>
Risk: Saved reports or proposed event records could add incorrect narrative facts to project memory if accepted without review. <br>
Mitigation: Require user confirmation before persistence and review proposed records before adding them to memory or event logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/narrative-drift-monitor) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown drift report with tables, evidence labels, trigger conditions, and handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Measured/User-provided/Estimated labels; saves reports or event proposals only after user confirmation.] <br>

## Skill Version(s): <br>
19.0.0 (source: evidence.json release.version, artifact frontmatter, target metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
