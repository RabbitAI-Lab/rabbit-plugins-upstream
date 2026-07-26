## Description: <br>
Repairs garbled speech-to-text input by fixing mistranscribed names, numbers, commands, dictated artifacts, recurring vocabulary, and noisy or mixed-language voice transcripts after they have been converted to text. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and voice-first agent operators use this skill to repair speech-to-text transcripts before responding, drafting dictated content, or acting on voice commands. It is especially useful for names, domain jargon, numbers, addresses, side-effectful commands, noisy transcripts, and recurring vocabulary corrections. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Local Listen files may contain names, jargon, language preferences, and correction history. <br>
Mitigation: Before installing, be comfortable with the skill reading and writing ~/Clawic/data/listen/; periodically inspect or delete those files if old corrections should not be retained. <br>
Risk: A repaired voice command could change the recipient, amount, file path, time, deployment target, or other side-effectful action. <br>
Mitigation: Confirm repaired values before irreversible or external actions, echo high-risk fields such as recipients and amounts, and use stricter confirmation settings when voice commands may send, delete, post, deploy, book, or pay. <br>
Risk: Noisy, truncated, or hallucinated speech-to-text output can create text the user did not intend. <br>
Mitigation: Drop known hallucination boilerplate, stop token-by-token repair when three or more tokens are suspect, and ask for a concise yes/no confirmation or the missing field instead of guessing. <br>


## Reference(s): <br>
- [ClawHub Listen skill page](https://clawhub.ai/ivangdavila/skills/listen) <br>
- [Listen homepage](https://clawic.com/skills/listen) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [Actions - side-effect confirmation](artifact/actions.md) <br>
- [Repair - candidate generation](artifact/repair.md) <br>
- [Numbers - digits, times, money, and addresses](artifact/numbers.md) <br>
- [Lexicon - persistence and lifecycle](artifact/lexicon.md) <br>
- [Degraded - noise, hallucinations, and truncation](artifact/degraded.md) <br>
- [Dictation - producing artifacts from voice](artifact/dictation.md) <br>
- [Tuning - fixing the engine instead of the transcript](artifact/tuning.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Natural-language agent guidance, repaired text, dictated Markdown or prose artifacts, confirmation prompts, and local configuration or lexicon entries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May store user-specific correction pairs and preferences in ~/Clawic/data/listen/ when the user confirms or reveals them.] <br>

## Skill Version(s): <br>
1.0.3 (source: evidence release and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
