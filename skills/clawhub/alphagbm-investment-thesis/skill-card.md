## Description: <br>
Records and tracks the reasons for buying a position and structured sell conditions attached to a company profile, monitoring them so a thesis can move from active to triggered when a condition fires. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[clementgu](https://clawhub.ai/user/clementgu) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Investors, traders, and research agents use this skill to create, review, update, and delete investment theses tied to AlphaGBM company profiles, including buy reasoning and exit triggers. It is useful for monitoring active versus triggered theses and surfacing the reason a sell condition fired. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can create, update, and hard-delete persistent investment thesis records. <br>
Mitigation: Require explicit user confirmation before delete actions and verify the numeric thesis id from a prior list or get operation before modifying records. <br>
Risk: The skill requires an AlphaGBM API key and may be used for real portfolio research. <br>
Mitigation: Install only after review, protect ALPHAGBM_API_KEY, and use the skill for clear investment research tracking requests rather than unsolicited financial guidance. <br>
Risk: Broad activation wording can match common investment thesis or exit-trigger requests. <br>
Mitigation: Confirm the intended ticker and write action before creating or updating thesis data. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/clementgu/skills/alphagbm-investment-thesis) <br>
- [AlphaGBM](https://alphagbm.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, API calls, configuration, guidance] <br>
**Output Format:** [Markdown summaries with JSON request and response examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires ALPHAGBM_API_KEY and an existing company profile before thesis creation; delete operations hard-delete records.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
