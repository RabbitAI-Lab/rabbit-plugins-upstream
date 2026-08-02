## Description: <br>
Perform forward and reverse geocoding using Nominatim and Open-Meteo APIs, supporting single and batch requests with CSV input and output. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and analysts use this skill to convert addresses or place names into coordinates, convert coordinates back into addresses, and process address lists from CSV files. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Addresses, place names, or coordinates are sent to Nominatim, Open-Meteo, or a configured external endpoint. <br>
Mitigation: Avoid confidential customer, home, or sensitive location datasets unless approved and provider logging and privacy terms are understood. <br>
Risk: Batch geocoding can disclose many locations and create local CSV or JSON result files. <br>
Mitigation: Review input sensitivity before batch runs and store or delete generated output files according to the relevant data-handling policy. <br>
Risk: Provider limits, timeouts, endpoint behavior, and documentation rough edges can affect completeness or reliability. <br>
Mitigation: Use documented rate limits, review failed rows or warnings, and validate results before relying on them in downstream workflows. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-geocoding-skill) <br>
- [Nominatim](https://nominatim.org/) <br>
- [Open-Meteo Geocoding API](https://open-meteo.com/en/docs/geocoding-api) <br>


## Skill Output: <br>
**Output Type(s):** [text, shell commands, configuration, code, guidance] <br>
**Output Format:** [Markdown guidance with CLI examples; the executed helper writes JSON or CSV result files.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May write geocoding result files and optional JSON run summaries to local paths.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
