## Description: <br>
Generate a TV-style weather infographic with a location-specific seasonal background. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[silverkiwi](https://clawhub.ai/user/silverkiwi) <br>

### License/Terms of Use: <br>


## Use Case: <br>
External users and developers use this skill to generate a visual weather forecast for a specific address, combining current conditions, a 7-day forecast, and a broadcast-style generated background. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the requested location and coordinates to Open-Meteo and uses the location in Gemini image generation prompts. <br>
Mitigation: Enter only locations you are comfortable sharing with Open-Meteo and Google Gemini. <br>
Risk: Gemini image generation can consume API quota while creating the infographic. <br>
Mitigation: Use a Gemini API key whose quota you are comfortable using. <br>
Risk: Installing dependencies into a shared Python environment can affect other projects. <br>
Mitigation: Install and run the skill in a virtual environment where possible. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/silverkiwi/skills/weather-infographic) <br>
- [Open-Meteo forecast API](https://api.open-meteo.com/v1/forecast) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Shell commands, Configuration] <br>
**Output Format:** [PNG image file with console status text] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires GEMINI_API_KEY and latitude, longitude, address, and output path arguments.] <br>

## Skill Version(s): <br>
1.0.2 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
