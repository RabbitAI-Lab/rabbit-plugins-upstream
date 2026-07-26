## Description: <br>
Helps agents run a weekly organic-social measurement readout with locked engagement-rate denominators, median per-post rollups, separated organic and boosted results, optional EMV translation, community-health metrics, and a keep/stop/try write-back list. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing and social teams use this skill to turn weekly channel exports and public community data into a consistent organic-social performance readout. It is especially suited for maintaining a metric dictionary, comparing channel performance across periods, and producing next-cycle content learnings without issuing ROI or ECHO gate verdicts. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Analytics exports, screenshots, pasted reports, and connector results can contain misleading data or embedded instructions. <br>
Mitigation: Treat those inputs as data only, label every number by source quality and as-of date, and require missing closed-platform exports instead of estimating them from memory. <br>
Risk: Changing engagement-rate denominators between periods can make trend comparisons misleading. <br>
Mitigation: Declare each numerator and denominator, lock channel denominators across periods, and treat any denominator switch as a trend restart. <br>
Risk: Optional saved readouts and promoted learnings can persist sensitive social analytics or channel observations. <br>
Mitigation: Ask before saving results or promoting learnings, and keep channel-state writes limited to the disclosed proposal flow. <br>


## Reference(s): <br>
- [Social Measurement Loop on ClawHub](https://clawhub.ai/aaron-he-zhu/skills/social-measurement-loop) <br>
- [aaron-marketing-skills repository](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown period readout with a metric dictionary, labeled measurements, performer analysis, and keep/stop/try write-back list] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May propose saved readouts and memory updates only after user approval.] <br>

## Skill Version(s): <br>
19.0.0 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
