## Description: <br>
Curates news, feeds, and industry sources into personalized recurring digests, including sourcing, filtering, ranking, verification, delivery, and preference learning. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
People who want recurring personal briefings use this skill to build daily, weekly, or on-demand digests around topics, competitors, industries, people, or markets they care about. It helps an agent source stories, filter exclusions, rank relevance, verify sensitive claims, adapt delivery format, and learn preferences over time. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may keep local digest preferences and sent-item history that reveal topics, source choices, timing, and user interests. <br>
Mitigation: Install only if this local history is acceptable, and periodically review or delete files under ~/Clawic/data/digest/ when preferences or retention should change. <br>
Risk: News digests can amplify stale, single-source, or misleading claims if sourcing and verification are weak. <br>
Mitigation: Require named sources for every item, deduplicate syndicated coverage, hold or hedge single-source claims, and use the correction guidance when a shipped item is wrong. <br>


## Reference(s): <br>
- [ClawHub Digest listing](https://clawhub.ai/ivangdavila/skills/digest) <br>
- [Clawic Digest skill page](https://clawic.com/skills/digest) <br>
- [Digest artifact: source guidance](artifact/sources.md) <br>
- [Digest artifact: verification guidance](artifact/verification.md) <br>
- [Digest artifact: delivery guidance](artifact/delivery.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown digest with sourced items, highlights, full digest sections, worth-noting entries, and channel-specific variants when relevant.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May rely on local preference, configuration, and sent-log files under ~/Clawic/data/digest/ to tune future digests.] <br>

## Skill Version(s): <br>
1.0.3 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
