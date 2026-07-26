## Description: <br>
Logo Design Guide helps agents plan and generate professional logos with AI image tools, covering logo types, prompt structure, color, sizing, delivery formats, platform options, and error handling. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Designers, developers, and brand builders use this skill to turn a logo request into AI image prompts, generation commands, iteration guidance, and delivery-format recommendations. It is most useful when an agent needs to advise on logo concepts, generate icon candidates, or adapt outputs for common brand and app surfaces. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: External image-generation calls can send brand prompts to third-party providers and consume paid quota. <br>
Mitigation: Review generated commands and provider choice before execution, use environment-managed API keys, and avoid sending sensitive brand material unless third-party processing is acceptable. <br>
Risk: AI image-generation tools may render text incorrectly or produce bitmap-only logo assets. <br>
Mitigation: Generate icon or symbol components with AI, add brand text manually in design software, and redraw or vectorize final artwork before delivery. <br>
Risk: Logo outputs may require trademark, brand, or print-production review before use. <br>
Mitigation: Run human trademark clearance, brand review, and production checks before relying on generated assets commercially. <br>


## Reference(s): <br>
- [DashScope Image Synthesis API](https://dashscope.aliyuncs.com/api/v1/services/aigc/text2image/image-synthesis) <br>
- [ClawHub skill listing](https://clawhub.ai/thcjp/skills/logo-design-guide) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with prompt examples and inline shell or API command snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide calls to external image-generation services using user-configured API keys.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; artifact frontmatter reports 0.2.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
