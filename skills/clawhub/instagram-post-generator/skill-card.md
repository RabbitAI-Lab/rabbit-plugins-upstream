## Description:

AI Instagram Post Generator creates editable, Instagram-ready posts and slides with generated content, captions, images, text blocks, storylines, backgrounds, and export-ready assets.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ai-hub-admin](https://clawhub.ai/user/ai-hub-admin)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate social media post assets from prompts, optional reference images, and design configuration for Instagram and related channels.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts, uploaded reference images, and design configuration are sent to the DeepNLP/OneKey/Craftsman service.

Mitigation: Use only content appropriate for that third-party service and avoid submitting sensitive or restricted material unless approved for the deployment.

Risk: The required OneKey Gateway API key could be exposed through prompts, logs, or committed files.

Mitigation: Store the API key as a secret, pass it through the documented environment variable, and do not paste it into prompts or source-controlled files.

Risk: Generated share URLs may be accessible to people who receive the link.

Mitigation: Share generated workspace links only with intended recipients and avoid using shared links for confidential outputs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ai-hub-admin/skills/instagram-post-generator)
- [Craftsman Social Media Posts Generator](https://craftsman-agent.aiagenta2z.com/app/social-media-posts)
- [Craftsman website](https://craftsman-agent.aiagenta2z.com)
- [OneKey Router endpoint](https://agent.deepnlp.org/agent_router)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with curl and npx command examples plus JSON request and response payloads.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The generated service output includes session identifiers, share URLs, image URLs, card counts, and editable page/layer configuration.]

## Skill Version(s):

1.0.0 (source: server release metadata and target metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
