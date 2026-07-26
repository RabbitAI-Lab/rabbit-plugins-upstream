## Description: <br>
Searches public web sources for current Hong Kong technology-sector dynamics and generates a structured daily pre-market opening brief. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and market-news analysts use this skill before the Hong Kong market open to collect current public news and produce a concise HK technology-sector brief. It is scoped to daily opening-note summaries, not historical analysis or portfolio-specific recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests memory-write capability without explaining a persistence feature. <br>
Mitigation: Install only if memory-write access is acceptable, or remove memory_write before use; require explicit user consent before saving any information. <br>
Risk: Market briefs generated from current public news can be incomplete, stale, or misleading. <br>
Mitigation: Verify important claims against primary market sources and do not treat the brief as portfolio-specific financial advice. <br>


## Reference(s): <br>
- [Sector Opening Note on ClawHub](https://clawhub.ai/terrycarter1985/skills/sector-opening-note) <br>
- [Yahoo Finance Technology Sector](https://finance.yahoo.com/sectors/technology) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, shell commands, guidance] <br>
**Output Format:** [Structured Markdown brief with concise sections for overview, news, companies, sentiment, risks, and catalysts.] <br>
**Output Parameters:** [1D; accepts date and market arguments.] <br>
**Other Properties Related to Output:** [Uses public web search for current HK technology-sector news; metadata requests memory_write without a stated persistence need.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
