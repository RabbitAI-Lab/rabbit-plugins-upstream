## Description: <br>
Builds, redesigns, and critiques presentation-grade PowerPoint slide decks using an interview, checkpoint, deck-generation, lint, render, and critic-review workflow. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[dong845](https://clawhub.ai/user/dong845) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Employees, external users, and developers use this skill to turn source material, existing decks, or open-ended presentation requests into audience-specific slide decks. It is intended for building, improving, reviewing, and handing off .pptx presentations with source fidelity and explicit review gates. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security scan flags broad local execution, network, persistence, and profile access. <br>
Mitigation: Install and run the skill first in trusted workspaces, keep sandboxing enabled where possible, and review generated files plus taste/profile writes before reuse. <br>
Risk: The skill may download assets, create files under Downloads, and use image-generation paths that can involve paid APIs if approved. <br>
Mitigation: Require explicit approval before network asset acquisition or paid image API use, and preserve source, license, and credit notes for sourced or generated visuals. <br>
Risk: Generated decks can be persuasive even when source material is incomplete or untrusted. <br>
Mitigation: Review source-trace checkpoints, claim ledgers, rendered slides, lint output, and independent critic findings before using decks for external or high-stakes communication. <br>


## Reference(s): <br>
- [Skill Definition](SKILL.md) <br>
- [Design Principles](references/design-principles.md) <br>
- [Content Plan Spec](references/content-plan-spec.md) <br>
- [Checkpoint Convention](references/checkpoint-convention.md) <br>
- [Review Rubrics](references/review-rubrics.md) <br>
- [File Inventory](references/file-inventory.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/dong845/skills/slide-maker) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance, checkpoint tables, Python build scripts, shell commands, generated files, and PowerPoint deck artifacts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces deck plans, review findings, rendered slide images, and .pptx deliverables when the host environment permits local file creation and rendering.] <br>

## Skill Version(s): <br>
4.2.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
