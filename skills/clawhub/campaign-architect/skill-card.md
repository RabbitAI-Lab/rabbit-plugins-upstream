## Description: <br>
Campaign Architect helps marketers and advertising teams design paid account structures, choose campaign types, map ad or asset groups, define targeting and exclusions, audit paid-organic overlap, and produce ROAS Audience structure notes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[aaron-he-zhu](https://clawhub.ai/user/aaron-he-zhu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Marketing teams, media buyers, and consultants use this skill before launch or account restructure to plan paid search, PMax, broad-match, targeting, exclusions, and paid-organic overlap checks. It produces a campaign structure and ROAS Audience notes for handoff to a full ad-account auditor. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Advertising and analytics exports can contain sensitive campaign strategy, keyword, placement, and performance data. <br>
Mitigation: Review data before installation and inspect any saved memory summaries when sensitive account information is used. <br>
Risk: Incomplete campaign, placement, or analytics evidence can lead to unsupported scoring or misleading structure recommendations. <br>
Mitigation: Require missing inputs to be marked as NEEDS_INPUT, UNDECIDED, or NOT_SCORED, and avoid emitting a ROAS Audience score from partial coverage. <br>
Risk: Optional read-only ad-platform connector workflows may expose account data through the user's configured connector environment. <br>
Mitigation: Use read-only connectors where available and rely on manual exports when connector access is not needed. <br>


## Reference(s): <br>
- [Campaign Architect on ClawHub](https://clawhub.ai/aaron-he-zhu/skills/campaign-architect) <br>
- [Project Homepage](https://github.com/aaron-he-zhu/aaron-marketing-skills) <br>
- [Google Ads MCP](https://developers.google.com/google-ads/api/docs/developer-toolkit/mcp-server) <br>
- [Meta Ad Library](https://www.facebook.com/ads/library/) <br>
- [Google Ads Transparency Center](https://adstransparency.google.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown with structured recommendations, status labels, and optional saved memory summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return NEEDS_INPUT, UNDECIDED, or NOT_SCORED instead of ROAS Audience scoring when required campaign or analytics evidence is incomplete.] <br>

## Skill Version(s): <br>
19.0.0 (source: server release metadata and artifact frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
