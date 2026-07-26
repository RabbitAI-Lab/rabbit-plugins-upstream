## Description: <br>
Use when computing or fixing vertical spacing (margins, padding, Auto Layout gap) between text blocks or components against a grid base, accounting for vertical-trim state on any text layers involved. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[monikazapisekstudio](https://clawhub.ai/user/monikazapisekstudio) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Product designers and design engineers use this skill to review, compute, and correct vertical spacing for cards, sections, articles, forms, and Figma Auto Layout frames against a grid base. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Figma write actions can change spacing, padding, paragraph spacing, or vertical-trim settings in selected frames. <br>
Mitigation: Review proposed values and authorize writes only when the selected frame and changes are intended. <br>
Risk: One missing-trim alert template is hard-coded in Polish. <br>
Mitigation: Adapt the alert wording to the user's locale before presenting it in non-Polish contexts. <br>


## Reference(s): <br>
- [Server-resolved GitHub provenance](https://github.com/monikazapisekstudio/design-engineering-playbook/tree/main/skills/typesetting-engine-skillset/vertical-spacing) <br>
- [ClawHub skill page](https://clawhub.ai/monikazapisekstudio/skills/vertical-spacing) <br>
- [Publisher profile](https://clawhub.ai/user/monikazapisekstudio) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Code, Guidance] <br>
**Output Format:** [Markdown with spacing values, CSS or Tailwind snippets, formulas, and review notes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include Figma read/write guidance; Figma writes require explicit user approval.] <br>

## Skill Version(s): <br>
0.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
