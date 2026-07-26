## Description: <br>
Extracts recipes from public Instagram reels by parsing captions, transcribing audio, analyzing frames, and formatting ingredients, instructions, and macros. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[kylelol](https://clawhub.ai/user/kylelol) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and agents use ClawdBites when they have a public Instagram reel and want a structured recipe with ingredients, instructions, macros, source attribution, and optional wishlist storage. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill downloads public reel media to /tmp and processes captions, audio, and frames. <br>
Mitigation: Use it only for public reels the user intentionally provides, and clear temporary media if local retention is a concern. <br>
Risk: Frame analysis may send extracted images to a vision model to read on-screen recipe text. <br>
Mitigation: Avoid using frame analysis on sensitive or private media, and review extracted text before relying on it. <br>
Risk: Wishlist and notes actions can persist recipes beyond the current conversation. <br>
Mitigation: Save recipes only after explicit user direction and keep saved recipe data limited to the intended wishlist or notes destination. <br>


## Reference(s): <br>
- [ClawdBites on ClawHub](https://clawhub.ai/kylelol/skills/clawdbites) <br>
- [ClawdBites publisher profile](https://clawhub.ai/user/kylelol) <br>
- [Clawdbot project](https://github.com/clawdbot/clawdbot) <br>


## Skill Output: <br>
**Output Type(s):** [Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown with structured recipe sections and inline shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May optionally save extracted recipes to a local wishlist JSON file when the user asks.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
