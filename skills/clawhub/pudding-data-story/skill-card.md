## Description: <br>
Builds or revises reader-first interactive data stories and visual essays with editorial framing, evidence checks, visual grammar, interaction design, implementation architecture, accessibility, mobile behavior, and QA. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[tseng71](https://clawhub.ai/user/tseng71) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External creators, editors, designers, and developers use this skill to plan, implement, revise, or audit Pudding-style interactive data stories. It helps turn sourced datasets into visual essays with claim ledgers, storyboards, scrollytelling architecture, accessible interactions, and QA notes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may be invoked for a wide range of visualization and data-story requests, including cases where its opinionated editorial workflow is not desired. <br>
Mitigation: Review whether implicit invocation is appropriate for the installation, and invoke or route the skill only for data-storytelling work that needs this editorial process. <br>
Risk: The local audit helper inspects supported text files under the supplied target path. <br>
Mitigation: Run the audit script only against project folders or story files that the agent is intended to inspect. <br>
Risk: Polished motion or interaction can make weak, stale, or incomplete evidence appear more certain than it is. <br>
Mitigation: Require a claim-to-source ledger, data notes, visible caveats, and data verification before treating a produced story as ready for publication. <br>


## Reference(s): <br>
- [Editorial workflow](references/editorial-workflow.md) <br>
- [AI data evidence guide](references/ai-data-evidence.md) <br>
- [Interaction and visual grammar](references/interaction-patterns.md) <br>
- [Technical template](references/technical-template.md) <br>
- [Deliverable templates](references/deliverable-templates.md) <br>
- [Pudding story pattern library](references/pudding-examples.md) <br>
- [The Pudding website starter](https://github.com/the-pudding/website) <br>
- [The Pudding pitch guidelines](https://pudding.cool/pitch/) <br>
- [The Pudding resources and process](https://pudding.cool/resources/) <br>
- [Can an AI make a data-driven, visual story?](https://pudding.cool/2024/07/ai/) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, markdown, code, shell commands, configuration] <br>
**Output Format:** [Markdown guidance with implementation code, configuration snippets, and shell commands where useful] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May produce story-brief.md, data-notes.md, storyboard.md, implemented story files, qa-notes.md, and audit findings.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
