## Description: <br>
Company Search Tool Free helps agents look up company information such as basic registration details, legal representatives, shareholders, investments, and business changes through a free company-information query workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill for intentional company-information lookups, including fuzzy company search, basic business registration details, legal representatives, shareholders, outward investments, and business changes. It is suited to personal due-diligence and lookup workflows, not broad SEO or unrelated search tasks. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Company or person names and identifiers may be sent to an external company-information API. <br>
Mitigation: Use the skill only for intentional company-information lookups and avoid submitting sensitive identifiers unless the user has approved the external query. <br>
Risk: The free edition's risk-screening and advanced due-diligence availability is inconsistent or unavailable in the evidence. <br>
Mitigation: Confirm backend behavior before relying on risk-screening results, and treat the free edition as a single-dimension company lookup tool unless stronger evidence is available. <br>
Risk: SEO-related trigger text appears in the artifact despite the company-search purpose. <br>
Mitigation: Route only company-information lookup requests to this skill and avoid using it for SEO or unrelated search tasks. <br>


## Reference(s): <br>
- [Detailed reference](references/detail.md) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/company-search-tool-free) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May call an external company-information API; the free edition uses a shared public key with a daily quota and supports an optional private API key.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
