## Description: <br>
Finds JD.com self-operated new-arrival products with filters for category, price, discount sorting, national subsidy and trade-in information, and returns formatted product results through a disclosed Tencent cloud proxy. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cn-shopping](https://clawhub.ai/user/cn-shopping) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External shoppers and shopping-assistant agents use this skill to discover JD.com self-operated new arrivals, compare discounted prices, and page through curated product results before deciding whether to visit purchase links. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Shopping queries and filters are sent through the publisher's Tencent cloud proxy. <br>
Mitigation: Install only if this proxy routing is acceptable, and avoid sending personal or sensitive shopping context through the skill. <br>
Risk: The reviewed artifacts include a hardcoded default proxy token and an externally hosted proxy endpoint. <br>
Mitigation: Prefer publisher-managed token rotation, documented retention practices, and a locked or reviewed proxy destination before broad deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cn-shopping/skills/jd-new-arrivals) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON] <br>
**Output Format:** [JSON string containing a human-readable summary and a JSON-encoded product-results payload] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include product names, prices, discount percentages, shop and category fields, image URLs, purchase URLs, and pagination summaries.] <br>

## Skill Version(s): <br>
1.2.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
