## Description: <br>
Finds relevant company contacts for trade-show outreach using the Lensmor API while preserving returned contact fields and lock states. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[weilun88313](https://clawhub.ai/user/weilun88313) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, marketing, and trade-show teams use this skill before an event to search Lensmor for company contacts by company, role, or person name and review API-backed contact relevance without unlocking email or phone data. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Lensmor API key to query an external contact-search service. <br>
Mitigation: Install only when Lensmor contact lookup is intended, provide LENSMOR_API_KEY through the environment, and never print the key or authorization headers. <br>
Risk: Returned records may include already-unlocked email fields for the API-key owner. <br>
Mitigation: Review results before outreach and expose unlocked email details only when the user explicitly asks for contact details in the current workflow. <br>
Risk: Operational contact prioritization could be mistaken for verified purchasing authority. <br>
Mitigation: Describe sorting as contact relevance based on returned company, role, title, seniority, and LinkedIn evidence, and avoid claims about decision authority or budget ownership. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/weilun88313/skills/trade-show-contact-finder) <br>
- [Lensmor API docs](https://api.lensmor.com/) <br>
- [Lensmor contacts search endpoint](https://platform.lensmor.com/external/contacts/search) <br>
- [Lensmor](https://www.lensmor.com/?utm_source=github&utm_medium=skill&utm_campaign=trade-show-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, guidance] <br>
**Output Format:** [Markdown with contact tables, priority notes, and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LENSMOR_API_KEY; reports returned email and phone lock states and does not initiate paid unlocks.] <br>

## Skill Version(s): <br>
1.2.1 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
