## Description: <br>
Routes AI image-editing requests by task, produces edit specifications and QA guidance, and sets honesty gates for inpainting, background removal, upscaling, outpainting, restoration, and retouching. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Creators, agencies, and social media operators use this skill to route existing-image edits to appropriate tools, write prompts or settings, and apply human review, rights, disclosure, and misrepresentation checks before publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Image edits can misrepresent products, people, or commercial claims if they conceal defects, hallucinate details, or omit required disclosures. <br>
Mitigation: Use faithful editing for accuracy-critical images, prohibit defect concealment and provenance stripping, verify source rights and market-specific disclosures, and require human review before publishing. <br>
Risk: Connected editing tools or generated specifications may produce flawed visual results or outdated engine-term assumptions. <br>
Mitigation: Treat the skill's output as routing and specification guidance, test on the user's own images, verify current engine terms, and have a human judge every result at full resolution. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/social-media-skills/skills/ai-image-editing) <br>
- [The reality of AI image editing in 2026](references/ai-image-editing-2026-reality.md) <br>
- [Scope, distinctions & connections](references/scope-and-connections.md) <br>
- [The task router, chains & worked examples](references/task-router-and-templates.md) <br>
- [The TOUCH framework](references/the-touch-framework.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown guidance with task routing, edit specs, QA checklists, and optional API-call parameters where connected.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires human review of image results at 100% zoom and separate verification of rights, disclosures, market rules, and engine terms.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
