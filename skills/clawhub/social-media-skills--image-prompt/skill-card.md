## Description: <br>
Helps agents turn a social-post visual need into a clear image brief, model-agnostic prompt, and tool-routing recommendation. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and social-media teams use this skill when a post needs a visual and the agent must decide whether to use an AI-generated image, write a useful image brief and prompt, and route to the right image or video tool. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may activate for broad image or graphic requests. <br>
Mitigation: Use it as a planning and routing aid for social-post visuals, then hand off generation to the appropriate tool-specific skill only when generation is warranted. <br>
Risk: AI-generated visuals can misrepresent real people, real places, copyrighted IP, or factual text and data. <br>
Mitigation: Gate against unnecessary generation, avoid real identifiable people and copyrighted IP, disclose AI imagery as required, and verify in-image text and data before publishing. <br>
Risk: Specific tool recommendations for image models can become stale. <br>
Mitigation: Re-verify model strengths and routing choices periodically while preserving the stable decision principle of matching the dominant visual requirement to the tool. <br>


## Reference(s): <br>
- [The Image Brief](references/the-image-brief.md) <br>
- [Prompt Anatomy](references/prompt-anatomy.md) <br>
- [Choosing the Tool](references/choosing-the-tool.md) <br>
- [Examples](references/examples.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Guidance] <br>
**Output Format:** [Markdown or plain-text guidance containing an image brief, natural-language prompt, routing recommendation, and handoff notes.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Does not generate images directly; it prepares and routes visual work to other tools or recommends a real asset when appropriate.] <br>

## Skill Version(s): <br>
1.0.1 (source: server-resolved release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
