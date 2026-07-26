## Description: <br>
Scores a named trade show against a company profile through Lensmor and returns a 0-10 exhibit fit recommendation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[weilun88313](https://clawhub.ai/user/weilun88313) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
B2B marketing, sales, and events teams use this skill to decide whether a specific trade show merits exhibit, attendance, or skip consideration before committing budget. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Lensmor API key and sends event lookup and fit-score requests to Lensmor's external service. <br>
Mitigation: Install only when the operator intends to use Lensmor, provide LENSMOR_API_KEY through the environment, and review responses to ensure the key is never exposed. <br>
Risk: The returned fit score is a profile signal, not a complete exhibit ROI or buyer-demand assessment. <br>
Mitigation: Use only the API-returned score, recommendation enum, and breakdown fields; validate budget, buyer fit, geography, and event strategy separately before committing. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/weilun88313/skills/trade-show-fit-score) <br>
- [Lensmor API docs](https://api.lensmor.com/) <br>
- [Lensmor](https://www.lensmor.com/?utm_source=github&utm_medium=skill&utm_campaign=trade-show-skills) <br>
- [Skill homepage](https://github.com/LensmorOfficial/trade-show-skills/tree/main/trade-show-fit-score) <br>
- [Example: Fit-Score Contract for a Named Show](examples/hannover-messe-iot-vendor.md) <br>


## Skill Output: <br>
**Output Type(s):** [markdown, API Calls, guidance] <br>
**Output Format:** [Markdown score card with event details, fit-score table, API recommendation enum, and concise interpretation.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scores and breakdown values come from the Lensmor API; the skill requires LENSMOR_API_KEY and must not reveal the key.] <br>

## Skill Version(s): <br>
1.2.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
