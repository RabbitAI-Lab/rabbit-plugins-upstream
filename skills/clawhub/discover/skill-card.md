## Description: <br>
Discover new ideas, sources, opportunities, and angles with durable watchlists, novelty rules, and heartbeat-backed finding logs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to keep track of ongoing discovery topics, find genuinely new angles or sources, and log only findings that change a decision, risk, opportunity, or next move. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent discovery can store sensitive interests or topic keywords in local watchlists and findings. <br>
Mitigation: Review activation preferences during setup and avoid adding sensitive topics unless local storage and public search use are acceptable. <br>
Risk: Recurring checks could become noisy or run beyond the user's intended scope. <br>
Mitigation: Enable heartbeat only after explicit approval, keep each topic tied to a clear novelty bar, and use HEARTBEAT_OK when nothing materially new appears. <br>
Risk: External lookups may send topic keywords and query variants to public search or community sites. <br>
Mitigation: Keep lookup scope narrow, tied to approved watchlist topics, and ask before using broader tools, paid services, third-party contact, or external commitments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/discover) <br>
- [Clawic skill page](https://clawic.com/skills/discover) <br>
- [Setup guide](setup.md) <br>
- [Discovery workflow](discovery-loop.md) <br>
- [Novelty test](novelty-test.md) <br>
- [Heartbeat rules](heartbeat-rules.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with local file templates and occasional shell command blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces local discovery state, watchlist entries, heartbeat status, and concise finding logs; no credentials are required by default.] <br>

## Skill Version(s): <br>
1.0.1 (source: release evidence and frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
