## Description: <br>
Generates and validates UI design deliverables, including interactive prototypes, annotated implementation specs, design tokens, structured spec JSON, assumptions logs, browser measurement reports, screenshots, and acceptance tests from text, screenshot, Sketch, or Figma inputs. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[hilper](https://clawhub.ai/user/hilper) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Designers, product teams, developers, and AI coding agents use this skill to turn UI requirements or source design inputs into high-fidelity prototypes and implementation-ready design specifications. It supports mobile H5 and web PC workflows, including design-system profile selection, token constraints, static QA, and browser-based acceptance evidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may create files under designs/<project> and start a localhost preview server. <br>
Mitigation: Review generated files and local preview commands before approval, and run previews in an appropriate local workspace. <br>
Risk: The skill may use connected Figma or GitHub tooling for links the user provides and may save approved design references for future reuse. <br>
Mitigation: Do not provide sensitive proprietary designs or approve stored references unless local reuse is acceptable. <br>
Risk: Generated UI specifications may contain inferred measurements, token mappings, or assumptions. <br>
Mitigation: Review assumptions.log, measured screenshots, browser measurement reports, and acceptance-test results before using the output for implementation. <br>


## Reference(s): <br>
- [Server-resolved source repository](https://github.com/hilper/design-hiker-skill) <br>
- [ClawHub skill page](https://clawhub.ai/hilper/skills/design-hiker-skill) <br>
- [Codex harness reference](references/codex.md) <br>
- [Claude Code harness reference](references/claude.md) <br>
- [Cursor harness reference](references/cursor.md) <br>
- [Universal design system component specs](design-system/universal/components.md) <br>
- [Universal design system usage guidelines](design-system/universal/usage-guidelines.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Code, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance plus generated HTML, CSS, JSON, log, screenshot, and JavaScript acceptance-test files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces deliverables under designs/<project-name>/ and relies on browser measurement evidence for acceptance.] <br>

## Skill Version(s): <br>
0.1.1 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
