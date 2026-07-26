## Description: <br>
Generate kinetic typography animations for expressive agent-to-human communication, including shareable links and GIF export URLs for announcements, greetings, alerts, and dramatic reveals. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andyed](https://clawhub.ai/user/andyed) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Agents and developers use this skill to make short human-facing messages more expressive through animated typography links or downloadable GIF workflows. It is best suited for concise greetings, announcements, celebrations, attention prompts, and dramatic reveals. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The helper script can run unintended local code when given a specially crafted message. <br>
Mitigation: Avoid running scripts/iblipper.sh on untrusted or copied message text until the encoder passes text as an argument or via stdin. <br>
Risk: Generated links expose message text through a URL and load an external renderer. <br>
Mitigation: Do not place sensitive text in generated links, and review links before sharing them with recipients. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/andyed/skills/iblipper) <br>
- [iBlipper renderer](https://andyed.github.io/iblipper2025/) <br>
- [iBlipper Examples](references/examples.md) <br>
- [iBlipper Emotion Presets](references/emotions.md) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Guidance] <br>
**Output Format:** [Plain URLs, Markdown links, and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Generated links load an external renderer; GIF export requires a browser download workflow.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
