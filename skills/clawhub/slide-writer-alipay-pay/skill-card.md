## Description: <br>
Turns plain-text ideas, outlines, and drafts into structured enterprise-style HTML presentation content through external Alipay services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[owenzhouzhou](https://clawhub.ai/user/owenzhouzhou) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and end users can use this skill to generate HTML presentation content from plain-text slide requests. It is intended for text-only inputs and does not support image, attachment, or document-file uploads. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Slide prompts and selected conversation context are sent to external Alipay services. <br>
Mitigation: Use only with non-sensitive text unless the publisher clarifies the remote service, retention, and consent model. <br>
Risk: Temporary request, session, and sent-context logs are written under /tmp during use. <br>
Mitigation: Run in an isolated environment and remove matching /tmp/conexa-S00000001784191990656-* files after use when local retention is not desired. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/owenzhouzhou/skills/slide-writer-alipay-pay) <br>


## Skill Output: <br>
**Output Type(s):** [text, code, shell commands] <br>
**Output Format:** [Plain text stream containing generated HTML presentation content, with shell commands used by the agent to submit and query the remote service.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Supports only plain-text prompts; the remote service response is read from an SSE text stream.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
