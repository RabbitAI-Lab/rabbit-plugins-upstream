## Description: <br>
Morning Intelligence interviews users about their role, topics, sources, exclusions, and format preferences, then produces a verified preference summary, a ready-to-paste daily briefing master prompt, and setup instructions. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mohitagw15856](https://clawhub.ai/user/mohitagw15856) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to build a personalized daily news briefing workflow. The skill conducts an interview, confirms the user's briefing preferences, and generates a reusable master prompt plus setup guidance for scheduled use. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A scheduled daily briefing can repeatedly gather news from the user's selected sources using the generated prompt, including any weak source, exclusion, or recency choices captured during setup. <br>
Mitigation: Review the generated master prompt before scheduling it, with particular attention to sources, exclusions, and recency rules. <br>


## Reference(s): <br>
- [Morning Intelligence ClawHub page](https://clawhub.ai/mohitagw15856/skills/morning-intelligence) <br>
- [Morning Intelligence homepage](https://mohitagw15856.github.io/pm-claude-skills/skill/morning-intelligence.html) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [Markdown containing a preference summary, fenced master prompt, and setup guide] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Includes a confirmation step before writing the final master prompt.] <br>

## Skill Version(s): <br>
50.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
