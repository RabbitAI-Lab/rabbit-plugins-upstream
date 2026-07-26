## Description: <br>
Conducts open-ended visual question answering on image content using computer vision and large language models to produce natural-language responses. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[18072937735](https://clawhub.ai/user/18072937735) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to answer natural-language questions about local or URL-based images and to retrieve prior visual question-answering reports from the associated cloud service. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Media, URLs, questions, report history, and an automatically managed identity are handled by the lifeemergence cloud service. <br>
Mitigation: Use the skill only when the publisher and service are trusted; avoid private images, internal URLs, and sensitive documents until retention, deletion, and token storage practices are confirmed. <br>
Risk: The skill can reuse local identity and token state while retrieving cloud history or running analyses. <br>
Mitigation: Run it in a controlled environment, review stored token and identity state before shared use, and clear credentials between users or tenants. <br>
Risk: The model-generated visual answers may be incomplete or incorrect for important decisions. <br>
Mitigation: Treat outputs as advisory and verify important facts or extracted details against the original image or another trusted source. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/18072937735/skills/smyx-visual-qa-analysis) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown or JSON analysis responses, including report links or history tables when returned by the service.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can process local image paths or public image URLs with a required user question; history-list output is fetched from the cloud service.] <br>

## Skill Version(s): <br>
1.0.10 (source: server release metadata; artifact frontmatter lists 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
