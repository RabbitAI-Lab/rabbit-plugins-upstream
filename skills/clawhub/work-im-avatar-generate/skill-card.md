## Description: <br>
Work Im Avatar Generate helps agents call WSD Social's avatar-generation API to turn a supplied photo into a polished business-style IM avatar. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[wsd-mj](https://clawhub.ai/user/wsd-mj) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to generate professional IM avatar headshots from an uploaded photo, image URL, or base64 image data, with optional styling instructions for background and outfit. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the chosen photo, image URL or base64 image data, styling request, and WSD API key to wsdsocial.com. <br>
Mitigation: Use only photos suitable for that provider, avoid images with sensitive background details, and review the provider's data handling terms before use. <br>
Risk: The WSD API key may be exposed if commands or environment output are pasted into shared logs or transcripts. <br>
Mitigation: Store WSD_API_KEY as a secret or local environment variable and avoid sharing command output that includes request headers. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/wsd-mj/skills/work-im-avatar-generate) <br>
- [Server-Resolved Source Repository](https://github.com/WSD-MJ/work-im-avatar-generate) <br>
- [WSD Social Skills Setup](https://ai.wsdsocial.com/skills) <br>
- [WSD Social Avatar Generation Endpoint](https://ai.wsdsocial.com/api/pub/skills/work-im-avatar-generate/_tool_85) <br>


## Skill Output: <br>
**Output Type(s):** [API Calls, Shell commands, Guidance] <br>
**Output Format:** [Markdown with bash examples and JSON response details] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Returns a generated avatar image URL; requires WSD_API_KEY and sends the chosen image data to ai.wsdsocial.com.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
