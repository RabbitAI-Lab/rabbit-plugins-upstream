## Description: <br>
Scrubs AI tells from LinkedIn drafts, rewrites or audits posts with tiered rules, and can compare detector-score disagreement across GPTZero, Originality.ai, ZeroGPT, Sapling, and Copyleaks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sergebulaev](https://clawhub.ai/user/sergebulaev) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and content teams use this skill to rewrite or audit LinkedIn drafts before publishing, preserving the user's claims while reducing AI-style vocabulary, cadence, emoji patterns, and format issues. It can also document disagreement across third-party AI detectors when a detector score needs context. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Rewrite modes may make aggressive changes to a draft's style. <br>
Mitigation: Review the diff before publishing and keep the original claim, meaning, and any user-specific voice cues that should remain. <br>
Risk: Detector tester API or manual modes can disclose draft text to named external detector services. <br>
Mitigation: Use --demo or local audit mode for private material, and only use API or manual mode when the text is appropriate to share with those services. <br>
Risk: The skill requests concrete details such as numbers, names, or anecdotes, which could be fabricated if not supplied by the user. <br>
Mitigation: Ask for missing facts or ship without them; do not invent numbers, named entities, or personal details. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/sergebulaev/skills/linkedin-humanizer) <br>
- [Scrub Rules](references/scrub-rules.md) <br>
- [Voice Fingerprint](references/voice-fingerprint.md) <br>
- [Tier Rationale](references/tier-rationale.md) <br>
- [Rules Explainer](references/rules-explainer.md) <br>
- [Emoji Patterns](references/emoji-patterns.md) <br>
- [Detector List](references/detector-list.md) <br>
- [Audit AI Tells](references/audit-ai-tells.md) <br>
- [Audit Checklist](references/audit-checklist.md) <br>
- [Detector Tester](sub-skills/detector-tester.md) <br>
- [Post Audit](sub-skills/post-audit.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with rewritten text, audit findings, diffs, detector summaries, and inline shell commands where needed] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include confidence labels such as human, mixed, or AI-likely; detector testing can also emit JSON when the bundled script is run with JSON output.] <br>

## Skill Version(s): <br>
1.0.9 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
