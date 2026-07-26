## Description: <br>
Fetches upcoming events from Luma for cities worldwide, including tech events, startup meetups, networking events, and conferences. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[regalstreak](https://clawhub.ai/user/regalstreak) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Agent users and event planners can use this skill to find, compare, and summarize public Luma events for one or more cities. It is useful for answering questions about upcoming tech events, meetups, conferences, and local event availability. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches public event data from lu.ma and depends on Luma's page structure remaining compatible with the bundled parser. <br>
Mitigation: Use the skill for public event discovery only, retry or inspect the latest page structure when parsing fails, and avoid excessive repeated fetching. <br>
Risk: Fetched event searches and possible planning context may be retained in ~/clawd/memory/luma-events.json. <br>
Mitigation: Review or delete the local event cache when past searches, cities, or plans should not be retained. <br>


## Reference(s): <br>
- [Luma](https://lu.ma) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Human-readable event summaries or JSON from the bundled Python script] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include event names, venues, dates, hosts, guest counts, ticket status, direct lu.ma links, and local event-cache entries.] <br>

## Skill Version(s): <br>
1.0.0 (source: target metadata, SKILL.md frontmatter, package.json, release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
