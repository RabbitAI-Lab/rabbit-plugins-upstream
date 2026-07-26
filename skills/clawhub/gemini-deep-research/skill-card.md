## Description: <br>
Performs complex, long-running research tasks using Gemini Deep Research Agent for multi-source synthesis, competitive analysis, market research, and technical investigations. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[arun-8687](https://clawhub.ai/user/arun-8687) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers, analysts, and researchers use this skill to run Gemini Deep Research jobs for multi-source synthesis, market or competitive analysis, and technical investigations. It saves markdown reports and full interaction metadata for review. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Research prompts and selected file-search context are sent to Google's Gemini service. <br>
Mitigation: Use only approved inputs for the intended Gemini environment and avoid sending sensitive material unless the service and account are authorized for it. <br>
Risk: Long-running research jobs may consume Gemini quota or incur cost. <br>
Mitigation: Monitor API usage and quota before running broad or repeated research jobs. <br>
Risk: Saved reports and response metadata may contain sensitive research content. <br>
Mitigation: Choose a private output directory and review generated markdown and JSON before sharing or committing them. <br>
Risk: Passing the API key as a command-line argument can expose it on shared machines. <br>
Mitigation: Prefer the GEMINI_API_KEY environment variable and avoid command-line secrets in shared environments. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/arun-8687/skills/gemini-deep-research) <br>
- [Google AI Studio API keys](https://aistudio.google.com/apikey) <br>
- [Gemini API interactions endpoint](https://generativelanguage.googleapis.com/v1beta/interactions) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, shell commands, guidance] <br>
**Output Format:** [Markdown report and JSON interaction metadata saved as timestamped files, with report text printed to stdout.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GEMINI_API_KEY; supports optional output format instructions, a Gemini file-search store, streaming progress, and a custom output directory.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
