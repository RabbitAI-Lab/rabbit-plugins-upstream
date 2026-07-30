## Description: <br>
Extracts writing style patterns from exemplar text into a reusable profile. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[athola](https://clawhub.ai/user/athola) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, writers, and content teams use this skill to analyze exemplar text, extract measurable style features, select representative passages, and produce reusable style profiles for consistent generation or editing. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Exemplar text may contain private, sensitive, or proprietary writing samples. <br>
Mitigation: Only provide writing samples that are appropriate for the agent to read and summarize into a reusable style profile. <br>
Risk: A generated style profile can misrepresent the target voice if metrics, exemplars, or anti-patterns are not reviewed. <br>
Mitigation: Review the generated profile and validate sample output against the source exemplars before reusing it. <br>
Risk: Broad triggers may activate the skill during unrelated writing tasks. <br>
Mitigation: Narrow activation triggers or invoke the skill explicitly when accidental style analysis would be disruptive. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/athola/skills/nm-scribe-style-learner) <br>
- [Project homepage](https://github.com/athola/claude-night-market/tree/master/plugins/scribe) <br>
- [Feature extraction module](artifact/modules/feature-extraction.md) <br>
- [Exemplar reference module](artifact/modules/exemplar-reference.md) <br>
- [Style application module](artifact/modules/style-application.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with YAML profile examples and inline shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces style profiles that combine quantitative metrics, exemplar passages, vocabulary preferences, structural guidance, punctuation patterns, anti-patterns, and validation notes.] <br>

## Skill Version(s): <br>
1.9.17 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
