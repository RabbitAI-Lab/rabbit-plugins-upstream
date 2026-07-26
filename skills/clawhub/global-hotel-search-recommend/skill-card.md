## Description: <br>
一次调用完成搜索与推荐，含预订链接和退改政策解读，自动识别商务/亲子/度假/背包场景智能推荐，3档价格分选，零配置即装即用。暑假出境游全球住宿推荐，覆盖200+国家 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and travel-planning agents use this skill to search global hotels, identify suitable options for business, family, vacation, backpacking, or general travel, and summarize prices, booking links, recommendation reasons, and cancellation policy details. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Hotel search details such as destination, dates, budget, and party composition are sent through the skill's cloud proxy to a hotel data provider. <br>
Mitigation: Send only the travel details needed for the search and avoid sensitive personal details that are not required for hotel selection. <br>
Risk: Prices, availability, booking links, and translated cancellation summaries can change or differ from the final booking page. <br>
Mitigation: Confirm price, availability, and the original cancellation policy on the booking page before making a reservation. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown text with tiered hotel recommendations, prices, booking links, tags, recommendation reasons, and cancellation summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Results may include real-time prices and booking links; the skill does not complete bookings directly.] <br>

## Skill Version(s): <br>
1.6.5 (source: server release evidence; artifact frontmatter and metadata contain older versions) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
