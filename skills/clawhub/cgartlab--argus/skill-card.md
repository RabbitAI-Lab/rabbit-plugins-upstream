## Description: <br>
Argus Design Review audits frontend code for design token usage, hardcoded values, dark mode coverage, accessibility, CSS consistency, semantic HTML, and framework API usage. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cgartlab](https://clawhub.ai/user/cgartlab) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineering teams use this skill to review frontend components, pages, and design systems for design-system consistency, accessibility issues, CSS quality, semantic markup, and stack-specific API mistakes. The skill returns prioritized findings with copy-ready fixes. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad review wording may activate the skill for general frontend review requests. <br>
Mitigation: Confirm the requested scope and files before relying on findings or applying generated fixes. <br>
Risk: Automated PR review mode depends on a separate GitHub App or action outside this inspected markdown-only package. <br>
Mitigation: Validate the external automation setup before treating PR gate results as authoritative. <br>
Risk: Copy-ready fixes can still be incomplete or over-broad for the target codebase. <br>
Mitigation: Review proposed changes against local design tokens, framework version, and tests before merging. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cgartlab/skills/argus) <br>
- [React reference](https://react.dev/reference) <br>
- [Vue guide](https://vuejs.org/guide) <br>
- [Svelte docs](https://svelte.dev/docs) <br>
- [Angular guide](https://angular.dev/guide) <br>
- [Astro docs](https://docs.astro.build) <br>
- [Lit docs](https://lit.dev/docs) <br>
- [MDN CSS documentation](https://developer.mozilla.org/docs/Web/CSS) <br>
- [TypeScript documentation](https://www.typescriptlang.org/docs/) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown review report with severity groups, issue blocks, reference links, and copy-ready code fixes] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May also be represented as pass/fail results and issue arrays when consumed through the skill manifest.] <br>

## Skill Version(s): <br>
0.3.1 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
