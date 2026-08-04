## Description: <br>
AI Podcast helps agents turn public PDF URLs or pasted text into multi-language, two-host conversational podcast episodes through the MagicPodcast API. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content creators, educators, researchers, and internal knowledge teams use this skill to convert source documents or text into shareable audio summaries and podcast-style conversations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided PDF URLs or pasted text are sent to MagicPodcast for remote processing. <br>
Mitigation: Use only content that is approved for external processing, and avoid confidential documents unless privacy and retention practices have been reviewed. <br>
Risk: The MagicPodcast API key could be exposed if it is placed in source files or shared output. <br>
Mitigation: Store the API key in environment variables and avoid writing secrets into repository files, prompts, or logs. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-podcast) <br>
- [MagicPodcast API](https://api.magicpodcast.app) <br>
- [MagicPodcast skill platform](https://www.magicpodcast.app/skill-platform) <br>
- [MagicPodcast app dashboard](https://www.magicpodcast.app/app) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with inline bash commands and external podcast links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May return MagicPodcast job status, dashboard URLs, share URLs, and error details from the external service.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
