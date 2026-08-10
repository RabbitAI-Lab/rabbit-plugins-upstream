## Description: <br>
Search YouTube and retrieve videos, shorts, comments, transcripts, streams, and channel data as structured JSON. 15 endpoints across video and channel surfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[scavio-ai](https://clawhub.ai/user/scavio-ai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to search YouTube through Scavio and retrieve structured video, comment, transcript, stream, and channel data for content research and agent workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Use requires a third-party Scavio API key and can spend API credits. <br>
Mitigation: Confirm SCAVIO_API_KEY is approved for the workspace and warn before broad pagination, transcript retrieval, or other credit-heavy requests. <br>
Risk: The streams endpoint can return direct playable or downloadable URLs for YouTube content. <br>
Mitigation: Use stream URLs only where the user has the right to access or download the content, and treat returned URLs as time-limited. <br>
Risk: Search terms and requested video or channel data are sent to Scavio. <br>
Mitigation: Avoid submitting private or sensitive search intent unless that use is acceptable under Scavio terms and privacy practices. <br>


## Reference(s): <br>
- [Scavio Documentation](https://scavio.dev/docs) <br>
- [Scavio Rate Limits](https://scavio.dev/docs/rate-limits) <br>
- [ClawHub Skill Page](https://clawhub.ai/scavio-ai/skills/scavio-youtube) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with JSON API shapes and inline bash/Python examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SCAVIO_API_KEY and returns Scavio API responses as structured JSON when executed by an agent.] <br>

## Skill Version(s): <br>
3.0.0 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
