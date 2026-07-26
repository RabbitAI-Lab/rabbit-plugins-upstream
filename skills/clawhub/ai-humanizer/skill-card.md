## Description: <br>
Humanize AI-generated text by detecting common LLM writing patterns, scoring text for AI-like signals, and providing rewrites or suggestions that sound more natural and specific. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[brandonwise](https://clawhub.ai/user/brandonwise) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Writers, editors, and agents use this skill to review AI-generated drafts, detect formulaic AI writing patterns, and produce more natural text while preserving the original meaning and intended tone. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Humanized text may be used in contexts with AI-assistance disclosure rules. <br>
Mitigation: Follow applicable disclosure policies and use the skill responsibly where disclosure is required. <br>
Risk: Optional standalone CLI development uses local Node tooling and dev dependencies. <br>
Mitigation: Review the source and update development dependencies before running tests or any Vitest UI/server workflow. <br>


## Reference(s): <br>
- [Wikipedia: Signs of AI writing](https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing) <br>
- [Copyleaks stylometric fingerprint research](https://arxiv.org/abs/2503.01659) <br>
- [blader/humanizer](https://github.com/blader/humanizer) <br>
- [Pattern reference](references/patterns.md) <br>
- [AI vocabulary reference](references/ai-vocabulary.md) <br>
- [Writing style guide](references/style-guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, JSON, Guidance, Shell commands, Configuration] <br>
**Output Format:** [Humanized text, markdown analysis reports, JSON analysis output, and concise writing guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Optional CLI modes can score, analyze, report, suggest, compute statistics, or apply safe autofixes.] <br>

## Skill Version(s): <br>
2.1.0 (source: package.json and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
