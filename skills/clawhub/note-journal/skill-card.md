## Description: <br>
Generates structured AI image prompts for notebook-style educational knowledge cards, check-in posters, teaching illustrations, practice pages, and answer explanation pages. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[fslong520](https://clawhub.ai/user/fslong520) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Educators, learning-content creators, and developers use this skill to turn a topic or lesson title into reusable prompt text for educational knowledge cards, daily-study posters, exercises, and answer-explanation visuals. It is designed for Chinese-first study materials, especially programming and CSP-J style learning content. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Broad Chinese visual-style triggers may invoke the skill when the user only mentions anime, cute, or pink visual styles. <br>
Mitigation: Review routing and trigger behavior before deployment where accidental invocation would disrupt other visual-design workflows. <br>
Risk: Generated educational prompt text can carry incorrect or unsuitable lesson details into downstream image generation. <br>
Mitigation: Review factual content, age fit, and classroom suitability before publishing generated cards or posters. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/fslong520/skills/note-journal) <br>
- [Publisher profile](https://clawhub.ai/user/fslong520) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, guidance] <br>
**Output Format:** [Markdown with structured prompt blocks and concise Chinese guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May ask for a missing required title before producing prompt text; does not require shell execution, credentials, persistence, or network access.] <br>

## Skill Version(s): <br>
1.7.0 (source: evidence release and skill frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
