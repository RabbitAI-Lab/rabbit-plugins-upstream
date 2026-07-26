## Description: <br>
Delegates tasks to Gemini CLI implementing delegation-core for Google's models. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to delegate large-context analysis, summarization, pattern extraction, and batch processing tasks to Gemini CLI when delegation-core selects Gemini or when Gemini's large context window is useful. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Prompts that use @path or recursive globs can include secrets or private data in Gemini CLI context. <br>
Mitigation: Review selected files first, use narrow file patterns, and avoid sending private or secret material to Gemini. <br>


## Reference(s): <br>
- [Gemini-Specific Configuration](artifact/modules/gemini-specifics.md) <br>
- [Conjure plugin homepage](https://github.com/athola/claude-night-market/tree/master/plugins/conjure) <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-conjure-gemini-delegation) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, shell commands, configuration] <br>
**Output Format:** [Markdown with inline bash code blocks] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May guide Gemini CLI prompts that include local files through @path or recursive glob patterns.] <br>

## Skill Version(s): <br>
1.9.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
