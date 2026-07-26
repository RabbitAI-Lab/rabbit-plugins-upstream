## Description: <br>
Create a structured global tech news briefing by running web searches for top tech trends, company announcements, and AI/quantum headlines. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[terrycarter1985](https://clawhub.ai/user/terrycarter1985) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to request concise global technology news briefings with key trends, company news, and takeaways. It supports current briefings and optional date-specific briefings. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Live external web searches may expose briefing topics to the search provider and can return incomplete, stale, or misleading news results. <br>
Mitigation: Avoid sensitive private briefing topics and review returned summaries before using them for decisions. <br>
Risk: The artifact uses shell execution to invoke web searches. <br>
Mitigation: Run the skill in a normal agent sandbox, keep required binaries limited to node and web_search, and review the script before deployment. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/terrycarter1985/skills/global-tech-briefing) <br>
- [Brave Search API](https://brave.com/search/api) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands] <br>
**Output Format:** [Structured text briefing with sections for key trends, company news, and key takeaways] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses Node.js and live web_search results; no API key is required for core searches.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
