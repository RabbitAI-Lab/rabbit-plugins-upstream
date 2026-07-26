## Description: <br>
Ai Podcast Free turns pasted plain text into a two-host conversational podcast through MagicPodcast and returns a shareable podcast link. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to convert articles, notes, or other pasted text into shareable audio podcasts after configuring a MagicPodcast API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided text is sent to MagicPodcast for processing. <br>
Mitigation: Do not submit secrets, private records, or regulated personal data unless MagicPodcast's data practices have been reviewed and the data is approved for sharing. <br>
Risk: The skill requires a MagicPodcast API key. <br>
Mitigation: Configure the API key locally and avoid committing it to source control. <br>
Risk: Podcast generation depends on MagicPodcast service availability and may take several minutes. <br>
Mitigation: Use the dashboard or job status endpoint for progress, avoid excessive polling, and retry only after checking network and service status. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-podcast-free) <br>
- [SkillHub homepage](https://skillhub.cn) <br>
- [MagicPodcast API key setup](https://www.magicpodcast.app/skill-platform) <br>
- [MagicPodcast dashboard](https://www.magicpodcast.app/app) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with bash and JSON snippets, API responses, and shareable podcast links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a MagicPodcast API key; podcast creation is asynchronous and returns status plus a shareable link when complete.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
