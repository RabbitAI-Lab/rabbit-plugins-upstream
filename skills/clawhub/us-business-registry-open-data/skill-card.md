## Description: <br>
Helps agents find, verify, and fetch bulk US business-registration open data from selected state Socrata portals for company registry analysis and lead-list workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[deciqai](https://clawhub.ai/user/deciqai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, analysts, and agents use this skill to identify commercially usable US state business-registry datasets, validate live endpoints, run sample or full pulls, and normalize records for analysis. It is suited to lead generation, formation-trend analysis, entity matching, registered-agent market maps, and vendor evaluation. <br>

### Deployment Geography for Use: <br>
United States <br>

## Known Risks and Mitigations: <br>
Risk: A full pull can transfer and store millions of public registry records. <br>
Mitigation: Run sample mode first, estimate storage and runtime, and set OUT_DIR deliberately before a full pull. <br>
Risk: A Socrata app token is sent to the configured government open-data portals when provided. <br>
Mitigation: Use only a token intended for those portals and avoid providing unrelated credentials. <br>
Risk: Some public datasets are deferred because licensing, availability, or access conditions are not suitable for this workflow. <br>
Mitigation: Use only enabled datasets with explicit public-domain or commercial-use terms, and confirm terms before enabling any deferred source. <br>


## Reference(s): <br>
- [Skill Page](https://clawhub.ai/deciqai/skills/us-business-registry-open-data) <br>
- [Sources](artifact/references/sources.md) <br>
- [Method in Action](artifact/examples/method-in-action-12m-pull.md) <br>
- [New York Active Corporations](https://data.ny.gov/Government-Finance/Active-Corporations-Beginning-1800/n9v6-gdp6) <br>
- [Colorado Business Entities](https://data.colorado.gov/Business/Business-Entities-in-Colorado/4ykn-tg5h) <br>
- [Pennsylvania Registered Businesses](https://data.pa.gov/Government-That-Works/Registered-Businesses-in-PA-Current-Monthly-County/xvd7-5r2c) <br>
- [Oregon Active Businesses](https://data.oregon.gov/Business/Active-Businesses-ALL/tckn-sxa6) <br>
- [Connecticut Business Registry Master](https://data.ct.gov/Business/Connecticut-Business-Registry-Business-Master/n7gp-d28j) <br>
- [Socrata SODA API Queries](https://dev.socrata.com/docs/queries/) <br>
- [Socrata App Tokens](https://dev.socrata.com/docs/app-tokens) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and Python configuration references] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce local JSONL files when the bundled fetcher is run by an agent.] <br>

## Skill Version(s): <br>
1.0.2 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
