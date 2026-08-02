## Description: <br>
Audits App Store and Google Play listings against ASO best practices and produces a prioritized optimization plan. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[coreyhaines31](https://clawhub.ai/user/coreyhaines31) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, marketers, and app teams use this skill to audit App Store or Google Play listings, compare competitors, and turn ASO findings into specific metadata, visual asset, keyword, and conversion recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Public store pages and screenshots can be incomplete, stale, or rendered in ways the agent cannot fully inspect. <br>
Mitigation: Note unavailable fields, work only from visible evidence, and ask the user to provide missing App Store Connect or Google Play Console details when they are important to the audit. <br>
Risk: ASO recommendations may be misleading if competitor context, brand maturity, or paid-tool metrics such as search volume and exact rankings are unavailable. <br>
Mitigation: State which metrics cannot be assessed, classify brand maturity before scoring, and frame keyword or competitor recommendations as evidence-based proposals for review and testing. <br>
Risk: The workflow may read local product-marketing context files when present. <br>
Mitigation: Keep audits scoped to the requested app listing and avoid including sensitive internal marketing details unless the user provides or approves that context for the report. <br>


## Reference(s): <br>
- [Apple App Store Specs and Guidelines](references/apple-specs.md) <br>
- [Google Play Specs and Guidelines](references/google-play-specs.md) <br>
- [ASO Benchmarks and Conversion Data](references/benchmarks.md) <br>
- [ASO Scoring Criteria](references/scoring-criteria.md) <br>
- [ASO Audit Report Template](references/report-template.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/coreyhaines31/skills/aso) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown audit report with scorecards, prioritized action plan, and platform-specific recommendations] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May depend on live public store pages, listing screenshots, competitor URLs, and user-provided console or marketing context.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release evidence; artifact metadata reports 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
