## Description: <br>
Transforms PDF URLs, pasted text, notes, and web links into two-host conversational podcasts through MagicPodcast and returns shareable podcast links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, content creators, educators, researchers, and knowledge teams use this skill to convert text or publicly reachable PDF content into multilingual conversational podcast episodes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided PDF URLs or pasted text are sent to MagicPodcast for external processing. <br>
Mitigation: Use only content approved for external processing and avoid regulated, confidential, or sensitive documents unless approval is in place. <br>
Risk: MagicPodcast API keys can be exposed if pasted into prompts, logs, or committed files. <br>
Mitigation: Store the API key in environment variables and avoid echoing or recording the key in generated commands or outputs. <br>
Risk: Callback URL behavior is not clearly documented in the evidence. <br>
Mitigation: Use callback URLs only when the receiving endpoint is controlled and can safely handle unknown payload details. <br>


## Reference(s): <br>
- [ai-podcast skill page](https://clawhub.ai/thcjp/skills/ai-podcast) <br>
- [MagicPodcast API service](https://api.magicpodcast.app) <br>
- [MagicPodcast skill platform](https://www.magicpodcast.app/skill-platform) <br>
- [MagicPodcast dashboard](https://www.magicpodcast.app/app) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Configuration, Guidance, Text] <br>
**Output Format:** [Markdown guidance with bash command examples and JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns job status details plus shareUrl or appUrl links when podcast generation completes.] <br>

## Skill Version(s): <br>
1.0.2 (source: ClawHub release metadata; artifact frontmatter reports 1.0.12) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
