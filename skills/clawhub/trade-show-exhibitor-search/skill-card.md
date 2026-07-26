## Description: <br>
Find exhibitors for a specific trade show or discover exhibitor companies across the Lensmor dataset. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[weilun88313](https://clawhub.ai/user/weilun88313) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, marketing, and event teams use this skill to list Lensmor exhibitor records for a named event or search the wider Lensmor dataset by company URL or target audience. It helps produce grounded exhibitor tables while preserving preview/full access boundaries and credit guidance. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Trade-show, company, or audience-search details are sent to Lensmor using the configured Lensmor API key. <br>
Mitigation: Use the skill only when sharing those details with Lensmor is acceptable, and keep LENSMOR_API_KEY configured through the environment without printing it. <br>
Risk: Expanded exhibitor access may consume Lensmor credits. <br>
Mitigation: Review unlock prompts and credit prices before approving any unlock action; the skill states that it does not unlock automatically. <br>
Risk: Cross-event discovery results may be mistaken for confirmed participation in a named event. <br>
Mitigation: Keep event-specific and cross-event results separate, and describe event participation only when matched event IDs or returned API provenance support it. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/weilun88313/skills/trade-show-exhibitor-search) <br>
- [Publisher profile](https://clawhub.ai/user/weilun88313) <br>
- [Lensmor API docs](https://api.lensmor.com/) <br>
- [Lensmor](https://www.lensmor.com/?utm_source=github&utm_medium=skill&utm_campaign=trade-show-skills) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown tables with API request guidance and concise next actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Lensmor event access metadata, preview/full counts, unlock credit guidance, and links returned by the API.] <br>

## Skill Version(s): <br>
1.2.1 (source: frontmatter and release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
