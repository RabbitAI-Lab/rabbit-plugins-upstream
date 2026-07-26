## Description: <br>
Retrieves Lensmor exhibitor recommendations for a specific trade show and clearly separates ranked matches from unranked fallback exhibitor records. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[weilun88313](https://clawhub.ai/user/weilun88313) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Sales, marketing, and business development users use this skill during pre-show planning to retrieve Lensmor event exhibitor recommendations, preserve returned ranks and scores, and avoid presenting unranked fallback exhibitor records as AI-ranked matches. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends trade-show names, filters, and the Lensmor bearer token to Lensmor's platform. <br>
Mitigation: Install only when Lensmor use is intended, keep LENSMOR_API_KEY scoped and secret, and avoid printing raw authorization headers. <br>
Risk: Broad invocation wording may cause the skill to activate in more pre-show recommendation contexts than desired. <br>
Mitigation: Review invocation behavior before deployment if tighter manual control is required. <br>
Risk: Fallback exhibitor records can be mistaken for ranked ICP recommendations. <br>
Mitigation: Use the skill's evidence gate: label rows as ranked only when recommendation metadata is populated, otherwise present them as unranked event exhibitor records. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/weilun88313/skills/trade-show-lead-recommender) <br>
- [Lensmor API Docs](https://api.lensmor.com/) <br>
- [Lensmor Platform Base URL](https://platform.lensmor.com) <br>
- [Lensmor](https://www.lensmor.com/?utm_source=github&utm_medium=skill&utm_campaign=trade-show-skills) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, API Calls, Shell commands, Guidance] <br>
**Output Format:** [Markdown with tables and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires LENSMOR_API_KEY and preserves Lensmor-provided ranks, scores, tiers, reasons, and fallback status without inference.] <br>

## Skill Version(s): <br>
1.2.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
