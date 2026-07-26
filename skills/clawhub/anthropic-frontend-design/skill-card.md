## Description: <br>
Create distinctive, production-grade frontend interfaces that avoid generic "AI slop" aesthetics. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[qrucio](https://clawhub.ai/user/qrucio) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and design-focused agents use this skill to build frontend components, pages, applications, and interfaces with distinctive typography, context-specific colors, intentional motion, accessibility checks, and production-grade implementation standards. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persisted design-system output can write MASTER.md or page-specific Markdown files outside the intended project location if output paths are chosen carelessly. <br>
Mitigation: Use --persist and --output-dir only with a project-owned or dedicated directory, then review generated MASTER.md and page files before relying on them. <br>
Risk: Generated frontend recommendations may be visually strong but still need validation for accessibility, responsiveness, and implementation quality. <br>
Mitigation: Run the skill's pre-delivery checklist, including contrast, responsive breakpoints, labels, alt text, cursor states, and stable hover behavior. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/qrucio/skills/anthropic-frontend-design) <br>
- [Publisher profile](https://clawhub.ai/user/qrucio) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown guidance with inline shell commands and generated frontend code or design-system files when requested] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled search tool returns local design reference matches and can optionally persist design-system Markdown files.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release metadata and artifact _meta.json) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
