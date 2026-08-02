## Description: <br>
Generate a structured daily morning brief for an industry vertical by searching public web sources and synthesizing the latest developments into a concise, actionable bulletin. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and industry analysts use this skill to produce concise daily news briefs for sectors such as new energy, EVs, solar, wind, hydrogen, semiconductors, and biotech. It is intended for public-source briefing and synthesis, not private data analysis, financial modeling, trading signals, or price prediction. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The bundled fetch helper makes public web requests based on user-provided industry or query terms. <br>
Mitigation: Review custom queries before running and use only public, non-sensitive topics; no API keys or private data are needed for the stated workflow. <br>
Risk: Fetched headlines may be incomplete, stale, duplicated, or insufficient for a reliable brief. <br>
Mitigation: Synthesize and deduplicate before publishing, prefer recent source dates, and keep source URLs attached to claims. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/terrycarter1985/skills/industry-morning-brief) <br>
- [Sources by Industry](references/sources.md) <br>
- [Reuters Renewable Energy](https://www.reuters.com/news/archive/renewableenergy) <br>
- [IEA News](https://www.iea.org/news) <br>
- [Reuters Technology](https://www.reuters.com/technology/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Markdown brief with section headings, bullet points, and source URL list] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled helper uses curl and public web requests; no API keys or private data are required for the stated workflow.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
