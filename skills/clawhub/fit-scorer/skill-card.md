## Description: <br>
Fit Scorer helps agents evaluate shortlisted influencers with a typed STAR Suitability read and a separately labeled campaign-fit ranking. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing and influencer teams use this skill to compare shortlisted creators for a campaign, preserve evidence-backed STAR Suitability item states, and keep campaign-specific commercial fit separate from the portable Suitability read. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may read campaign context, creator records, and optional analytics data for shortlisted influencers. <br>
Mitigation: Confirm the data scope before installation and provide only relevant campaign and creator information. <br>
Risk: Influencer recommendations can be misleading when evidence is missing or when campaign commercial fit is confused with STAR Suitability. <br>
Mitigation: Require dated evidence or gap reasons for Suitability items, keep commercial_fit_score separate, and treat Unknown coverage as blocking a complete Suitability read. <br>
Risk: Saved reports or promoted picks could preserve an unreviewed recommendation. <br>
Mitigation: Save reports and promote top picks only after explicit user authorization. <br>


## Reference(s): <br>
- [Fit Scorer release page](https://clawhub.ai/aaron-he-zhu/skills/fit-scorer) <br>
- [Project homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Scoring templates](references/scoring-templates.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown guidance with structured Suitability item states, commercial-fit tables, and outreach recommendations.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Report files are written only with explicit user authorization; creator picks require separate authorization before promotion.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
