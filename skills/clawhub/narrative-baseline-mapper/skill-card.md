## Description: <br>
Maps the current messaging across owned surfaces, labels each observed line by evidence strength, compares it with the intended message, and freezes a drift baseline for later narrative review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, product, and narrative teams use this skill before a repositioning or canon update to inventory what owned touchpoints say today, identify gaps against the intended message, and create a dated baseline for future drift checks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read pasted or scraped messaging surfaces that contain untrusted content. <br>
Mitigation: Use it only on owned or controlled surfaces, treat pasted and scraped content as evidence rather than instructions, and review the resulting baseline before reuse. <br>
Risk: Saved baselines or proposed claim records can preserve inaccurate or unverified marketing claims. <br>
Mitigation: Require user confirmation before saving memory updates, keep unverifiable claims marked [needs source], and route them to the claim review workflow rather than treating them as approved facts. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/aaron-he-zhu/skills/narrative-baseline-mapper) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration] <br>
**Output Format:** [Markdown narrative baseline document with inventory tables, gap reads, source labels, and a handoff summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Labels each data point as Measured, User-provided, or Estimated; flags unverifiable claims as [needs source].] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
