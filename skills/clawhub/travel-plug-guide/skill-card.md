## Description: <br>
Provides offline plug type, voltage, frequency, travel adapter, and appliance safety guidance for 200+ countries and regions using IEC-standard data. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[travel-skills](https://clawhub.ai/user/travel-skills) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External travelers and travel-planning agents use this skill to check destination plug standards, voltage and frequency, adapter needs, and whether common appliances are safe to use abroad. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The current version unexpectedly reads a PROXY_TOKEN environment variable and includes a hardcoded fallback token despite being an offline travel utility. <br>
Mitigation: Review before installation and remove the PROXY_TOKEN lookup and hardcoded fallback token before broad use. <br>
Risk: Plug, voltage, and hotel socket details may vary by region, building, or venue, which could lead to incorrect adapter or transformer choices. <br>
Mitigation: Treat the output as travel guidance and confirm device labels, local standards, and accommodation details before using high-power or single-voltage appliances. <br>


## Reference(s): <br>


## Skill Output: <br>
**Output Type(s):** [text, guidance] <br>
**Output Format:** [JSON-formatted text in Chinese] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Offline lookup results for plug type, voltage, frequency, adapter recommendations, and device-safety checks.] <br>

## Skill Version(s): <br>
1.0.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
