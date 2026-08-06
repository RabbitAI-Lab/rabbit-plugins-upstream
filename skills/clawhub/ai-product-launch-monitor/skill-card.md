## Description: <br>
One-command AI product launch monitoring pipeline that collects AI product launches from RSS feeds, enriches them with web search, captures screenshots, and scores trends. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to monitor recent AI product launches, enrich launch candidates with search context, capture optional page screenshots, and produce a ranked launch report for follow-up analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill makes outbound requests to RSS feeds, search providers, and product pages, and custom feeds can cause linked pages to be opened during screenshot capture. <br>
Mitigation: Run it only where those network destinations are acceptable; use --no-search or --no-screenshots in restricted environments and avoid untrusted custom feeds. <br>
Risk: The skill writes generated reports, JSON data, and optional screenshots to a local output directory. <br>
Mitigation: Use a dedicated output directory and review generated files before sharing or importing them into downstream workflows. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, configuration, shell commands, guidance] <br>
**Output Format:** [Markdown report, structured JSON, optional PNG screenshots, and command-line status output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Writes report.md, launches.json, and optional screenshots/*.png under the configured output directory.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
