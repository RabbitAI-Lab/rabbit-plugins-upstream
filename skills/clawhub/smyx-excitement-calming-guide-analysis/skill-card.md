## Description:

Analyzes pet activity-area images or videos to assess over-excitement behaviors, produce structured reports, and recommend calming interventions such as voice prompts, gentle tones, lighting changes, or pheromone-device actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui)

### License/Terms of Use:

MIT-0

## Use Case:

External pet owners, boarding centers, daycare staff, and trainers use this skill to review pet activity footage, identify over-excitement patterns, and receive behavior-safety calming guidance. Results are for behavior safety support and are not medical advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Pet-area videos or URLs are processed by lifeemergence.com cloud services.

Mitigation: Use only footage you have permission to process, and avoid sensitive household footage unless consent, retention, deletion, and data-use terms are clear.

Risk: The skill may create or reuse a persistent internal identity and store tokens or profile data in a workspace SQLite database.

Mitigation: Run the skill in an isolated workspace or account, review local token storage before deployment, and clear local credentials when the skill is no longer needed.

Risk: Behavior-safety guidance may be over-relied on for pets that repeatedly cannot calm down or may have health issues.

Mitigation: Treat outputs as behavior-safety guidance only, and involve a veterinarian or qualified behavior trainer when behavior is persistent, severe, or health-related.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-excitement-calming-guide-analysis)
- [Skill demo](https://lifeemergence.com/sample.html)
- [Pet excitement calming API documentation](artifact/references/api_doc.md)
- [Common analysis API documentation](artifact/skills/smyx_analysis/references/api_doc.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files]

**Output Format:** [Markdown text with structured JSON analysis content and report links; optional saved text output file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Accepts local video files or public video URLs; history queries return cloud report records.]

## Skill Version(s):

1.0.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
