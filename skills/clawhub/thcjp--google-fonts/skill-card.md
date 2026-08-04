## Description: <br>
Provides Google Fonts selection, pairing, loading optimization, variable font, subsetting, and self-hosting guidance for agents. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[thcjp](https://clawhub.ai/user/thcjp) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and designers use this skill to ask an agent for practical Google Fonts recommendations, CSS/HTML loading patterns, font pairing choices, variable font guidance, subsetting advice, and self-hosting considerations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill appears to be a Google Fonts reference but declares broad read, write, execution, API, and credential-related powers that are not clearly scoped to font guidance. <br>
Mitigation: Use it as Markdown guidance only unless a task explicitly requires an action, and prefer a revised release that limits those powers to user-approved font-related work. <br>
Risk: Font-loading, subsetting, or self-hosting recommendations may be incorrect for a specific browser, region, privacy posture, or deployment environment. <br>
Mitigation: Review generated CSS, HTML, and shell commands before applying them, and test font loading, fallback behavior, CORS, caching, and privacy requirements in the target environment. <br>


## Reference(s): <br>
- [Google Fonts API](https://fonts.googleapis.com) <br>
- [Google Fonts CSS2 example from skill](https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Lora:wght@500;700&display=swap) <br>
- [ClawHub skill page](https://clawhub.ai/thcjp/skills/google-fonts) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Code, Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline HTML, CSS, and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include font pairing tables, loading recommendations, self-hosting steps, and troubleshooting guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
