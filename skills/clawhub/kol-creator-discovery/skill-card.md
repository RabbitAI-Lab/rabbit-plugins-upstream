## Description: <br>
Discovers similar KOL creators and API-sourced creator contact emails from TikTok, Instagram, or YouTube profile URLs and returns an outreach-ready report without inventing missing data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[baofeng-tech](https://clawhub.ai/user/baofeng-tech) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, marketing teams, and developer/operators use this skill to research creator prospects, find similar YouTube or TikTok creators, enrich results with API-sourced contact data, and prepare a Markdown outreach list. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires an AIsa API key for external API access. <br>
Mitigation: Provide AISA_API_KEY only through the normal secret mechanism and do not print, log, or commit the key. <br>
Risk: Reports can contain personal creator contact data. <br>
Mitigation: Review output paths and share or store reports only when there is an appropriate business purpose and authorization. <br>
Risk: Email lookups and creator enrichment may consume API quota. <br>
Mitigation: Keep enrichment scope explicit and confirm larger batches before making many lookup calls. <br>
Risk: Missing contact data could be mistaken for incomplete processing. <br>
Mitigation: Preserve the skill's distinction between Not found and Lookup failed, and do not infer or manufacture email addresses. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/baofeng-tech/skills/kol-creator-discovery) <br>
- [AIsa](https://aisa.one) <br>
- [WaveInflu Email Lookup](https://aisa.one/docs/api-reference/waveinflu/post_waveinflu-email-lookup) <br>
- [WaveInflu Similar Creators](https://aisa.one/docs/api-reference/waveinflu/post_waveinflu-similar) <br>
- [AIsa API Reference](https://aisa.one/docs/api-reference) <br>
- [Local API reference](references/api-reference.md) <br>
- [Report template](references/report-template.md) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, JSON, Guidance] <br>
**Output Format:** [Markdown report with an optional JSON file] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include API-sourced creator contact data, lookup status, coverage notes, and quota limitations.] <br>

## Skill Version(s): <br>
1.0.0 (source: release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
