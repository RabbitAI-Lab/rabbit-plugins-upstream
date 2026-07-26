## Description: <br>
Searches Xiaohongshu (XHS/RedNote) notes by keyword, applies supported page filters, and returns enriched note metadata including body text, tags, media URLs, timestamps, and engagement counts. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[browseract-cli](https://clawhub.ai/user/browseract-cli) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, analysts, and developers use this skill to automate logged-in Xiaohongshu keyword searches and collect structured note metadata from pages they can access in the browser. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Logged-in Xiaohongshu extraction can implicate user privacy and platform-policy obligations. <br>
Mitigation: Run only with the user's informed login, keep searches narrowly scoped, and collect only data needed for the user's stated task. <br>
Risk: The artifact contains throughput guidance that could be used to evade rate limits. <br>
Mitigation: Do not use stealth multi-session throughput patterns; use conservative pacing and stop if Xiaohongshu presents limits, blocks, or additional consent prompts. <br>
Risk: Full-field extraction may collect personal-content metadata such as author identifiers, avatars, locations, and engagement counts. <br>
Mitigation: Minimize or redact personal fields unless they are necessary, and avoid retaining credentials, session data, or unnecessary personal data. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/browseract-cli/skills/xiaohongshu-search-full) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/browseract-cli) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples and JSON result objects from browser-executed extraction scripts] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires a logged-in Xiaohongshu browser session; extracted media URLs may be time-limited.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
