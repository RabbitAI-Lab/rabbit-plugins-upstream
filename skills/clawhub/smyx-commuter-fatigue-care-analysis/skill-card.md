## Description: <br>
Analyzes smart-home living-room video from the first 30 minutes after an office worker arrives home to estimate fatigue signals, produce a fatigue index, and suggest gentle care actions such as warm lighting, soothing music, or a supportive voice prompt. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and smart-home builders use this skill to process a living-room video file or video URL and return structured fatigue observations, a fatigue level, recommended care actions, report links, and report-history output. The outputs are care suggestions and visual or optional audio observations, not medical diagnoses. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends sensitive home-camera video or video URLs to the Life Emergence cloud service. <br>
Mitigation: Install only after reviewing the provider's retention, deletion, access-control, and data-sharing practices; avoid using private home footage until those controls are acceptable. <br>
Risk: The skill creates or reuses an internal account identity and persists tokens or report history locally. <br>
Mitigation: Run it in an isolated workspace or account, avoid shared machines for sensitive use, and review or clear local token and report storage during uninstall or rotation. <br>
Risk: Fatigue estimates and care prompts could be inaccurate or be mistaken for health diagnosis. <br>
Mitigation: Treat outputs as non-diagnostic care suggestions; keep human review for repeated high-fatigue patterns and direct users to qualified health or EAP support when appropriate. <br>
Risk: Automated smart-home care actions could become intrusive if triggered too often or when the user wants quiet. <br>
Mitigation: Respect opt-out, pause, and silence controls; keep intervention caps and quiet periods enabled before connecting speakers, lights, or other devices. <br>


## Reference(s): <br>
- [API Interface Documentation](references/api_doc.md) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/smyx-commuter-fatigue-care-analysis) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, json, guidance] <br>
**Output Format:** [Structured JSON text with optional Markdown history/report output and report links] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write the returned report text to a user-selected output file; history lookup returns a structured report list.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release metadata; artifact frontmatter lists 1.0.5) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
