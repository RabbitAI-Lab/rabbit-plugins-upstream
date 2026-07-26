## Description: <br>
Enriches leads by finding verified emails from websites, Instagram, Hunter.io, and email patterns, then formats deduplicated lead data for Notion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[visualdeptcreative](https://clawhub.ai/user/visualdeptcreative) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Sales, marketing, and operations users use this skill to enrich lead records with likely contact emails and prepare deduplicated batches for Notion. It guides agents through website, Instagram, Hunter.io, and pattern-based email discovery with confidence and batching rules. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Lead domains are sent to Hunter.io during enrichment. <br>
Mitigation: Use the skill only when sharing those domains with Hunter.io is acceptable for the lead data being processed. <br>
Risk: Hunter.io and Notion access can expose or modify more data than intended if credentials are broad. <br>
Mitigation: Use a scoped Hunter.io API key and grant Notion access only to the intended lead database. <br>
Risk: Saved enriched-lead JSON files may contain contact details. <br>
Mitigation: Delete or protect saved batch files when they are no longer needed. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/visualdeptcreative/skills/data-enricher) <br>
- [Hunter.io Domain Search API](https://api.hunter.io/v2/domain-search) <br>


## Skill Output: <br>
**Output Type(s):** [JSON, Files, Guidance] <br>
**Output Format:** [JSON lead records with concise processing logs] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Batches of up to 10 leads; Hunter.io lookups limited to 10 per session with 5 seconds between API calls.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
