## Description: <br>
Scans Amazon category landscapes to identify trending subcategories, emerging niches, demand shifts, brand consolidation, new entrants, price movement, and margin changes. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[apiclaw](https://clawhub.ai/user/apiclaw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External sellers, ecommerce analysts, and agents use this skill to scan Amazon parent categories, compare subcategory momentum, detect market shifts, and prepare trend reports for product selection or market-entry timing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a ZooData API key and can make credit-consuming API calls. <br>
Mitigation: Review planned scans and credit estimates before broad or multi-call runs, and provide only a ZooData key intended for this use. <br>
Risk: The bundled shared ZooData CLI exposes broader workflows than the advertised trend scanner. <br>
Mitigation: Limit use to the documented trend-scanning commands and review the skill before deployment. <br>
Risk: Changing ZOODATA_BASE_URL can redirect requests away from the disclosed ZooData API. <br>
Mitigation: Leave ZOODATA_BASE_URL unset unless the destination is explicitly trusted. <br>
Risk: The skill stores scan state in local scan-data files. <br>
Mitigation: Review retained baseline, watchlist, and history files before sharing or publishing the skill workspace. <br>


## Reference(s): <br>
- [ZooData Skills GitHub repository](https://github.com/SerendipityOneInc/ZooData-Skills) <br>
- [ZooData API key setup](https://zoodata.ai/en/api-keys) <br>
- [ZooData API documentation](https://api.zoodata.ai/api-docs) <br>
- [Market trend scanner field reference](references/reference.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown trend report with tables, API provenance, credit usage, and optional shell commands or scheduling configuration] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Output language follows the user's input language; reports include confidence labels and a data provenance table.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release metadata and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
