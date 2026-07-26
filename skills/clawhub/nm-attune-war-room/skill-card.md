## Description: <br>
Convenes a multi-LLM expert panel to pressure-test hard-to-reverse decisions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and technical decision makers use this skill to assess reversibility, convene multiple AI expert perspectives, pressure-test trade-offs, and synthesize a decision for high-stakes architecture or strategy choices. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Project context may be sent to configured external model tools during expert-panel analysis. <br>
Mitigation: Install only when this data flow is acceptable, and avoid using the skill with confidential or restricted project material unless the configured tools are approved. <br>
Risk: Decision summaries may be offered for GitHub Discussions publication by default. <br>
Mitigation: Decline publishing for confidential work and review any proposed discussion body before allowing publication. <br>
Risk: The artifact documents a GLM fallback that skips permissions. <br>
Mitigation: Do not use the permission-skipping fallback or alias unless it has been explicitly reviewed and approved for the environment. <br>
Risk: Local decision archives can retain sensitive deliberation content. <br>
Mitigation: Review and delete local Strategeion archives when they contain sensitive material or are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-attune-war-room) <br>
- [Clawdis homepage](https://github.com/athola/claude-night-market/tree/master/plugins/attune) <br>
- [Farnam Street: Reversible and Irreversible Decisions](https://fs.blog/reversible-irreversible-decisions/) <br>
- [One-Way and Two-Way Door Decision-Making](https://tapandesai.com/one-way-two-way-doors-decision-making/) <br>
- [Amazon Type 1 vs Type 2 Decisions](https://ashikuzzaman.com/2025/03/03/amazons-type-1-vs-type-2-decisions-a-framework-for-effective-decision-making/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown decision documents with command examples and local session records.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce reversibility scores, expert-panel summaries, premortems, dissenting views, and optional GitHub Discussion summaries.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence; artifact frontmatter reports 1.9.8) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
