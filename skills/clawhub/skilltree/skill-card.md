## Description: <br>
SkillTree analyzes recent chat history to recommend an agent class, track abilities, and adapt growth paths with visible feedback. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[0xraini](https://clawhub.ai/user/0xraini) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and agent developers use SkillTree to personalize an assistant by analyzing recent conversations, choosing an agent class and growth path, and producing status, ability, weekly, and share cards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill profiles recent chat history and may store evolving personal context. <br>
Mitigation: Use only with explicit user consent, periodically review or reset stored profile data, and avoid retaining sensitive or inaccurate details. <br>
Risk: Some growth-path behavior encourages fewer confirmation asks or acting before asking. <br>
Mitigation: Require explicit approval before emails, messages, calendar or file changes, public posts, purchases, share cards, and other external side effects. <br>
Risk: Personalization may reinforce incorrect inferred preferences or unsuitable assistant behavior. <br>
Mitigation: Expose profile summaries for review and use the documented reset or rollback paths when behavior drifts. <br>


## Reference(s): <br>
- [SkillTree ClawHub Listing](https://clawhub.ai/0xraini/skills/skilltree) <br>
- [README.en.md](artifact/README.en.md) <br>
- [SKILL.en.md](artifact/SKILL.en.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Configuration, Guidance] <br>
**Output Format:** [Markdown and plain-text agent responses with inline status cards, command names, and profile summaries.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read recent chat history and persist profile or snapshot data when the host agent supports file storage.] <br>

## Skill Version(s): <br>
1.1.0 (source: server evidence release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
