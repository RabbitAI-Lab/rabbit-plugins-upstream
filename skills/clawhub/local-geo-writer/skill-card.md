## Description: <br>
Local Geo Writer helps generate SEO/GEO-oriented Chinese marketing articles for local businesses and content teams. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[g620710](https://clawhub.ai/user/g620710) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and marketing teams use this skill to create local-business content for search visibility, AI-search visibility, and content marketing workflows. Users should review generated articles before publication. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The security review says this commercial GEO article generator can send credentials and article inputs to an under-disclosed HTTP backend. <br>
Mitigation: Do not use real API keys, confidential business data, or customer content until the publisher clarifies the backend, uses HTTPS, and documents data handling. <br>
Risk: The security review says the documentation and runtime behavior do not line up. <br>
Mitigation: Review the installed source and test commands with non-sensitive sample content before relying on the documented workflow. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/g620710/skills/local-geo-writer) <br>
- [DeepSeek API endpoint referenced by the skill](https://api.deepseek.com/v1) <br>
- [Configured GEO service endpoint](http://47.109.39.255:8765/api/v4) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Files, Shell commands, Configuration guidance] <br>
**Output Format:** [Plain text or Markdown articles, with optional file output from the command-line tool] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires python3 and a GEO_USER_KEY environment variable for authenticated generation.] <br>

## Skill Version(s): <br>
2.1.2 (source: server evidence release.version) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
