## Description: <br>
AI Image Editing routes existing-image edit requests such as inpainting, background removal, upscaling, outpainting, restoration, and retouching to appropriate tools while preserving human review and image-integrity checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[social-media-skills](https://clawhub.ai/user/social-media-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, social media operators, and agents use this skill to classify an existing-image editing task, choose the right editing lane, write the edit specification, and hand off results for human quality review and publishing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Edited real photos can misrepresent products, people, results, or provenance. <br>
Mitigation: Use faithful upscaling for accuracy-critical images, avoid defect concealment, preserve watermarks and provenance, confirm source-image rights, and apply required AI or retouching disclosures. <br>
Risk: Generative editing and creative upscaling can introduce hallucinated details or identity drift. <br>
Mitigation: Make one targeted change at a time, verify faces, text, lighting, perspective, and batch consistency at 100% zoom, and require the human or a person familiar with the subject to judge final fidelity. <br>
Risk: Connected third-party editing or publishing tools may process images outside the skill itself. <br>
Mitigation: Confirm connected tool terms, privacy posture, and commercial-rights requirements before routing source images or publishing outputs. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/social-media-skills/skills/ai-image-editing) <br>
- [The reality of AI image editing in 2026](references/ai-image-editing-2026-reality.md) <br>
- [Scope, distinctions & connections](references/scope-and-connections.md) <br>
- [The task router, chains & worked examples](references/task-router-and-templates.md) <br>
- [The TOUCH framework](references/the-touch-framework.md) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, API calls, configuration] <br>
**Output Format:** [Markdown guidance with edit specifications, routing decisions, QA checks, and optional API execution details where connected] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires human review of edited images at 100% zoom before publishing.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
