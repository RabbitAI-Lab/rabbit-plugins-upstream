## Description: <br>
Generates platform-specific social media captions for photography across Instagram, Flickr, X, Glass, Reddit, and other publishing communities, adapting tone, format, tags, and equipment details to each platform. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External photographers, social media managers, and content teams use this skill to draft tailored captions for a single photo or photo set across multiple publishing communities without reusing the same wording. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requests command execution and file-writing authority that is broader than its caption-writing purpose clearly requires. <br>
Mitigation: Run it with minimal agent permissions and do not grant command execution, file write access, API keys, callbacks, or scheduling authority unless the publisher narrows and documents those behaviors. <br>
Risk: Photo context can include private locations, people, clients, or unpublished campaign details. <br>
Mitigation: Provide only the context needed for captioning and review generated captions before publishing them to public platforms. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/photo-captions) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown or plain text caption drafts grouped by platform] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include separate captions for up to 12 platforms, hashtag choices, equipment lines, titles, topic suggestions, and character-limited variants.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata; artifact frontmatter reports 1.2.6) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
