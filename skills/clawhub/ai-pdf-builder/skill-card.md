## Description: <br>
AI-powered PDF generator for legal docs, pitch decks, and reports. SAFEs, NDAs, term sheets, whitepapers. npx ai-pdf-builder. Works with Claude, Cursor, GPT, Copilot. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nextfrontierbuilds](https://clawhub.ai/user/nextfrontierbuilds) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use this skill to generate professional PDFs, Markdown drafts, summaries, and enhanced documents for legal, investor, technical, and business workflows. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Installing and running npm, Pandoc, and LaTeX tooling can execute software on the user's machine. <br>
Mitigation: Install from trusted sources, review commands before execution, and use an isolated environment when appropriate. <br>
Risk: AI features may send prompts or document content to Anthropic/Claude. <br>
Mitigation: Use AI features only with documents approved for that data sharing, protect ANTHROPIC_API_KEY, and avoid confidential legal or investor materials unless approved. <br>
Risk: Generated legal, investor, or business documents may be inaccurate or unsuitable for a specific use. <br>
Mitigation: Have qualified reviewers check generated SAFEs, NDAs, term sheets, reports, and summaries before relying on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nextfrontierbuilds/skills/ai-pdf-builder) <br>
- [ai-pdf-builder npm package](https://www.npmjs.com/package/ai-pdf-builder) <br>
- [ai-pdf-builder project repository](https://github.com/NextFrontierBuilds/ai-pdf-builder) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and TypeScript examples; generated document outputs may be PDF or Markdown.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require Pandoc, LaTeX, npm package execution, and ANTHROPIC_API_KEY for AI features.] <br>

## Skill Version(s): <br>
1.2.3 (source: release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
