## Description: <br>
Turns PDFs, text, and links into two-person conversational podcasts for personal creators who want to quickly produce audio content. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and creators use this skill to guide an agent through creating shareable two-person podcast audio from text, PDF URLs, notes, or links through MagicPodcast. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends user-provided text or PDF URLs to MagicPodcast for podcast generation, which may expose sensitive or confidential content to an external service. <br>
Mitigation: Confirm before sending documents or links, avoid confidential material, and use the skill only when the user explicitly requests podcast creation. <br>
Risk: The security review flags broader activation and vague modify, delete, import, and export language outside the stated podcast use case. <br>
Mitigation: Treat those broad operations as out of scope unless the skill is updated with precise limits, and review commands before execution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/ai-podcast-tool-free) <br>
- [MagicPodcast skill platform](https://www.magicpodcast.app/skill-platform) <br>
- [MagicPodcast app](https://www.magicpodcast.app/app) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Shell commands, Configuration, API calls, Text] <br>
**Output Format:** [Markdown guidance with bash and curl command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns podcast creation status and share links when the external API succeeds.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and skill metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
