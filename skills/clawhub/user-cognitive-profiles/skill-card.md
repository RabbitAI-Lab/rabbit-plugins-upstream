## Description: <br>
Analyze ChatGPT conversation exports to discover cognitive archetypes and optimize AI-human communication patterns. Enables personalized agent interactions based on detected user profiles. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[sebastianffx](https://clawhub.ai/user/sebastianffx) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use this skill to locally analyze exported ChatGPT conversations, identify recurring communication archetypes, and produce profile data or prompt snippets that help agents adapt their interaction style. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: ChatGPT exports, generated profiles, and prompt snippets can contain sensitive personal information. <br>
Mitigation: Run the analysis locally, review and redact generated content, and minimize what is copied into SOUL.md, AGENTS.md, repositories, or hosted agents. <br>
Risk: The optional WildChat test script intentionally fetches and profiles an external dataset. <br>
Mitigation: Do not run test_wildchat.py unless external dataset access and profiling are intended. <br>
Risk: Unpinned Python dependencies can change behavior across environments. <br>
Mitigation: Use a virtual environment and consider pinning dependencies before running the analysis. <br>


## Reference(s): <br>
- [ClawHub skill listing](https://clawhub.ai/sebastianffx/skills/user-cognitive-profiles) <br>
- [Methodology](artifact/references/methodology.md) <br>
- [README](artifact/README.md) <br>
- [scikit-learn K-Means documentation](https://scikit-learn.org/stable/modules/clustering.html#k-means) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, configuration, guidance] <br>
**Output Format:** [JSON profile files, Markdown prompt snippets, and console summaries] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Profiles include archetype breakdowns, confidence scores, context-shift signals, communication preferences, and agent-calibration guidance.] <br>

## Skill Version(s): <br>
1.0.0 (source: evidence.release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
