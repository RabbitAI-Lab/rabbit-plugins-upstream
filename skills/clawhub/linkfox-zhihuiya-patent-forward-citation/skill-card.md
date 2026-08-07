## Description: <br>
Queries Zhihuiya patent forward-citation data so an agent can report the patents and non-patent literature cited by one or more patent IDs or publication numbers. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[linkfox-ai](https://clawhub.ai/user/linkfox-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, patent analysts, and developers use this skill to retrieve and present cited patent and non-patent literature for specified patent IDs or publication numbers. It is suited to citation detail retrieval and prior-art reference review, not broader patent validity, family, legal-status, or landscape analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends queried patent identifiers to a paid external LinkFox/Zhihuiya patent lookup service using LinkFox API credentials. <br>
Mitigation: Use credentials only in trusted environments, warn users that queries may consume credits, and get confirmation before additional cost-generating lookups. <br>
Risk: The script writes full API responses and cache entries to local LinkFox data directories. <br>
Mitigation: Run the skill in an appropriate workspace and review, retain, or delete saved response and cache files according to the user's data-control requirements. <br>
Risk: The skill documentation directs agents to send feedback about interactions to LinkFox when feedback conditions are detected. <br>
Mitigation: Review or disable feedback reporting where strict data-control boundaries apply, and avoid including sensitive user content in feedback. <br>


## Reference(s): <br>
- [智慧芽专利引用查询 API 参考](artifact/references/api.md) <br>
- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-zhihuiya-patent-forward-citation) <br>
- [LinkFox patent forward citation API endpoint](https://tool-gateway.linkfox.com/zhihuiya/patentForwardCitation) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, JSON, Markdown, Files, Guidance] <br>
**Output Format:** [Markdown guidance with JSON API responses and saved local JSON files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Accepts patentId or patentNumber values, supports comma-separated batches up to 100 entries, caches responses for 24 hours, and summarizes large responses unless inline output is requested.] <br>

## Skill Version(s): <br>
1.0.6 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
