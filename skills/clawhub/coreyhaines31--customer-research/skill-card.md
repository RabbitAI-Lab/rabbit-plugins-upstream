## Description: <br>
Guides agents through customer research by analyzing existing assets and gathering new research from online sources such as forums, review sites, and communities. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coreyhaines31](https://clawhub.ai/user/coreyhaines31) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing, product, growth, and research teams use this skill to turn customer interviews, surveys, support tickets, reviews, and public community sources into grounded customer insights. It supports research synthesis, voice-of-customer quote banks, personas, jobs-to-be-done maps, competitive intelligence summaries, and research gap analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Customer interviews, support tickets, survey exports, and similar inputs can contain confidential or personal information. <br>
Mitigation: Review and redact sensitive materials before sharing them with an agent, and limit analysis to files and context that are directly relevant to the research task. <br>
Risk: Public-source research can overrepresent vocal reviewers, technical communities, or people with strong opinions. <br>
Mitigation: Use the skill's bias checks, source weighting, confidence labels, and recency windows when presenting insights. <br>
Risk: Personas, messaging, or product conclusions can be misleading when based on too few data points or stale evidence. <br>
Mitigation: Require multiple independent data points per segment, label low-confidence findings, and treat proxy-source personas as provisional until first-party evidence is available. <br>


## Reference(s): <br>
- [Customer Research Source Guides](artifact/references/source-guides.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/coreyhaines31/skills/customer-research) <br>
- [Reddit Subreddit Search](https://www.reddit.com/subreddits/search) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Text, Markdown] <br>
**Output Format:** [Markdown research plans, synthesis reports, quote banks, persona documents, jobs-to-be-done maps, competitive intelligence summaries, or research gap analyses.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include confidence labels, source/date fields, verbatim quotes, bias notes, and recency guidance when source material supports them.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata; artifact metadata version 2.0.1) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
