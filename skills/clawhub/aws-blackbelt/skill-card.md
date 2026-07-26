## Description: <br>
AWS Black Belt服务 helps agents search AWS Black Belt Online Seminar content by keyword and retrieve video transcripts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cainingnk](https://clawhub.ai/user/cainingnk) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and external users can use this skill to find AWS Black Belt seminar materials and retrieve Japanese video transcripts through the Xiaobenyang third-party API. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a Xiaobenyang third-party API key and may persist it in a local .env file. <br>
Mitigation: Use a limited API key if available, avoid committing generated .env files, and prefer setting XBY_APIKEY through the runtime environment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cainingnk/skills/aws-blackbelt) <br>
- [Xiaobenyang API key site](https://xiaobenyang.com) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown summaries of search results and transcripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Search results include seminar metadata, PDF links, and YouTube links when returned by the API; transcript output is supported for Japanese seminar videos.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
