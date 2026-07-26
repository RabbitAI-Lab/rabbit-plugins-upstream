## Description: <br>
Track and manage your habits using the Beaver Habit Tracker API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[legionspace-hackathon](https://clawhub.ai/user/legionspace-hackathon) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to list Beaver Habits, view a recent completion table, and mark named habits complete or incomplete through the Beaver Habit Tracker API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill uses BEAVERHABITS_API_KEY to read habit data and mark habits complete or incomplete. <br>
Mitigation: Keep the API key private, use the default service or a trusted HTTPS SERVER_URL, and phrase update requests clearly with the habit name and date. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/legionspace-hackathon/skills/beaverhabits) <br>
- [Beaverhabits Homepage](https://github.com/daya0576/beaverhabits) <br>
- [Beaver Habit Tracker](https://beaverhabits.com) <br>
- [Beaver Habit Tracker API Documentation](https://beaverhabits.com/docs) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands] <br>
**Output Format:** [Markdown with ASCII tables and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires curl and BEAVERHABITS_API_KEY; SERVER_URL may point to the default hosted service or a trusted self-hosted instance.] <br>

## Skill Version(s): <br>
1.0.0 (source: target metadata and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
