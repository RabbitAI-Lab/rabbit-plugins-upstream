## Description: <br>
Generates new content drafts based on reference content analysis, including analysis of reference URLs, pattern extraction, context questions, meta-prompt creation, and multiple draft variations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[vincentchan](https://clawhub.ai/user/vincentchan) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Writers, marketers, founders, and content teams use this skill to analyze high-performing reference content and generate new articles, posts, tweets, or related drafts that follow the discovered structure and positioning. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill fetches user-provided URLs, so private, internal, signed, or tokenized links could expose sensitive reference content. <br>
Mitigation: Use public reference links when possible and avoid private, internal, signed, or tokenized URLs. <br>
Risk: Generated markdown drafts may contain confidential positioning, strategy, or unpublished content supplied during context gathering. <br>
Mitigation: Review generated files before sharing them and delete local drafts that contain sensitive material. <br>
Risk: X/Twitter links may be transformed through FxTwitter handling. <br>
Mitigation: Review the transformed URL behavior before providing sensitive or restricted X/Twitter references. <br>


## Reference(s): <br>
- [Content Anatomy Generator](references/content-anatomy-generator.md) <br>
- [Content Context Generator](references/content-context-generator.md) <br>
- [Content Deconstructor](references/content-deconstructor.md) <br>
- [Meta Prompt Generator](references/meta-prompt-generator.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance, files] <br>
**Output Format:** [Markdown files and conversational prompts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Fetches user-provided reference URLs, may use FxTwitter for X/Twitter links, saves timestamped local markdown files, and generates three draft variations.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
