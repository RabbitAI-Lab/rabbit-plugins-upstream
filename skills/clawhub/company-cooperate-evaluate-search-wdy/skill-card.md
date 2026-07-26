## Description: <br>
Uses WenDaoYun enterprise data to assess whether a company is suitable as a customer, supplier, partner, collaborator, or investment target. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[rose-develop](https://clawhub.ai/user/rose-develop) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Business, procurement, sales, compliance, and investment users can ask for a company cooperation assessment. The skill searches for the target company, waits for user confirmation, then summarizes cooperation risk, key signals, limitations, and recommended next actions. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Unauthorized or unnecessary use of enterprise due-diligence data. <br>
Mitigation: Confirm the user is authorized to query and use WenDaoYun enterprise data for the stated due-diligence purpose before relying on results. <br>
Risk: Exposure of the WenDaoYun API key. <br>
Mitigation: Keep WENDAOYUN_API_KEY private, store it as an environment variable, and rotate it through the WenDaoYun platform if disclosure is suspected. <br>
Risk: A fuzzy search result may identify the wrong company. <br>
Mitigation: Show candidate companies and wait for explicit user confirmation before calling the detailed cooperation-evaluation endpoint. <br>
Risk: A cooperation decision may be misleading if based only on available WenDaoYun data. <br>
Mitigation: State that the assessment is for reference only, include evidence limitations, and recommend follow-up checks or materials where risk remains. <br>


## Reference(s): <br>
- [fuzzy-search-org API reference](references/fuzzy-search-org.md) <br>
- [get-cooperate-evaluate API reference](references/get-cooperate-evaluate.md) <br>
- [WenDaoYun API key portal](https://open.wintaocloud.com/home) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance, Configuration instructions] <br>
**Output Format:** [Markdown assessment with a conclusion, key signals, limitations, and next actions] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires WENDAOYUN_API_KEY and user confirmation before detailed company lookup; avoids long raw data dumps unless requested.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
