## Description: <br>
Looks up digital movie and TV deals, prices, charts, recommendations, price history, and all-time-low signals across CheapCharts-supported stores using the public CheapCharts API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tracerman](https://clawhub.ai/user/tracerman) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill when an agent needs to answer questions about digital movie or TV prices, current sales, price drops, all-time lows, price history, charts, or recommendations. The skill can return deal summaries and guide API or script-based CheapCharts lookups. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Movie or TV title queries may be sent to CheapCharts, and occasional IMDb checks may be used for Movies Anywhere-style compatibility checks. <br>
Mitigation: Use the skill only when those public title queries are acceptable for the user or workflow. <br>
Risk: The DetailData endpoint used for all-time-low and price-history enrichment is unofficial and may change or fail. <br>
Mitigation: Treat price-history enrichment as best effort; fall back to public CheapCharts API data or clearly state when history or ATL checks are unavailable. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/tracerman/cheapcharts-skill/tree/main/skills/cheapcharts) <br>
- [ClawHub skill page](https://clawhub.ai/tracerman/skills/cheapcharts) <br>
- [CheapCharts AI documentation](https://www.cheapcharts.com/us/ai) <br>
- [CheapCharts website](https://www.cheapcharts.com) <br>
- [CheapCharts API Reference](references/API.md) <br>
- [CheapCharts API Pitfalls](references/PITFALLS.md) <br>
- [CheapCharts API Recipes](RECIPES.md) <br>
- [CheapCharts Extras](references/EXTRAS.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tables, JSON, shell commands, and concise text guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May perform public web/API requests to CheapCharts and occasional IMDb checks; no credentials or API keys are required.] <br>

## Skill Version(s): <br>
0.1.6 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
