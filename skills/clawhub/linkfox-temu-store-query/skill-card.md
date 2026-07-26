## Description: <br>
Filters and retrieves Temu store records by keyword, site, category, hosting mode, sales, revenue, ratings, reviews, followers, product counts, and listing dates. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
E-commerce analysts and agents use this skill to find, filter, rank, and inspect Temu stores across sites, categories, fulfillment modes, sales metrics, revenue, ratings, reviews, followers, product counts, and listing dates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Queries use LinkFox paid Temu store analytics access and can consume credits based on returned store count. <br>
Mitigation: Confirm the requested page size, expected result count, and credit cost with the user before running queries. <br>
Risk: Full API responses may be saved locally and can end up outside the active project if normal output paths are unavailable. <br>
Mitigation: Tell the user where response files are saved and avoid running broad queries when the destination is unclear. <br>
Risk: The documented feedback endpoint can send a summary of user intent and results to LinkFox. <br>
Mitigation: Use the feedback endpoint only after the user explicitly agrees to send that information. <br>


## Reference(s): <br>
- [Temu Store Query API Reference](references/api.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/linkfox-ai/skills/linkfox-temu-store-query) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Files, Shell commands, Guidance] <br>
**Output Format:** [JSON API responses, saved JSON files, concise text summaries, and Markdown guidance with shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The optional CLI can save full API responses to a LinkFox session data directory, print small responses inline, and summarize larger responses.] <br>

## Skill Version(s): <br>
1.0.7 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
