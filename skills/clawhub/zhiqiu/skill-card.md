## Description: <br>
Zhiqiu is an industry-analysis agent skill that helps produce structured market, value-chain, competitive landscape, strategic group, trend, and risk reports from current public research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tuobadaidai](https://clawhub.ai/user/tuobadaidai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Use for industry research, market sizing, value-chain analysis, competitive landscape reviews, Porter's Five Forces analysis, strategic group mapping, industry trend tracking, and high-level comparisons between sectors. The skill is not intended for company strategy diagnosis, organization diagnosis, simple one-off data lookup, or policy Q&A. <br>

### Deployment Geography for Use: <br>
User-selected based on the requested industry scope, with support for China, global, or regional analysis when the user defines the geography. <br>

## Known Risks and Mitigations: <br>
Risk: The skill may perform web research, so industry figures can become stale or vary across public sources. <br>
Mitigation: Review cited sources, confirm publication dates, and re-run research when core data exceeds the freshness expectations described by the skill. <br>
Risk: The optional financial-report-fetching dependency may introduce separate operational or trust considerations if enabled. <br>
Mitigation: Review and install the optional dependency only when report and annual-filing retrieval is needed for the analysis. <br>
Risk: Generated industry analysis may include directional judgments that users could over-apply to investment or company strategy decisions. <br>
Mitigation: Treat outputs as research support, verify material claims independently, and use dedicated strategy or financial diligence workflows for decisions. <br>


## Reference(s): <br>
- [Zhiqiu Skill on ClawHub](https://clawhub.ai/tuobadaidai/skills/zhiqiu) <br>
- [tuobadaidai Publisher Profile](https://clawhub.ai/user/tuobadaidai) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, text, shell commands, guidance] <br>
**Output Format:** [Structured Markdown reports, comparison tables, tracking-update tables, concise scan summaries, and cited source notes.] <br>
**Output Parameters:** [Industry or sector name; optional module focus such as market, competition, value chain, strategic groups, or trends; optional modes such as --quick, --compare, and --track; geography and time window when supplied by the user.] <br>
**Other Properties Related to Output:** [Outputs emphasize current public-source research, source attribution, explicit data freshness checks, cross-validation of key figures, and clear separation between industry analysis and company-specific strategy advice.] <br>

## Skill Version(s): <br>
1.2.1 <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
