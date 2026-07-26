## Description: <br>
Audits brand narrative truth, message-system coherence, and measured effectiveness as separate TALE profiles without merging them into one composite score. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, narrative, and product teams use this skill to audit positioning truth, canon coherence, flagship surface alignment, and message-effectiveness evidence as separate TALE profiles. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may inspect sensitive marketing canon, surface drafts, or experiment evidence supplied in the working context. <br>
Mitigation: Install and run it only in workspaces where that material may be reviewed by the agent. <br>
Risk: Audit reports can be persisted under memory/audits/narrative when explicitly authorized. <br>
Mitigation: Grant persistence only when a durable audit record is intended, and review the target path before authorizing the write. <br>
Risk: Standalone installs cannot compute deterministic scores, gate verdicts, or persistent artifacts without the full runtime. <br>
Mitigation: Treat standalone results as NOT_SCORED observation sets until they can be replayed in a full plugin or repository install. <br>
Risk: A narrative-system audit could be mistaken for launch readiness, social operations, or market-effectiveness proof. <br>
Mitigation: Use the skill only for the requested TALE truth, system, effectiveness, or full narrative profile, and route other decisions to the appropriate specialist skill. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/aaron-he-zhu/skills/narrative-quality-auditor) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Standalone Auditor Runtime](references/auditor-runtime.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown audit report or structured observation text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May persist a permissioned v3 audit artifact only after explicit authorization; standalone mode returns NOT_SCORED when deterministic runtime is unavailable.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
