## Description: <br>
Weave multiple maps, text and charts into a scroll-driven storytelling HTML page. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ruiduobao](https://clawhub.ai/user/ruiduobao) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, data journalists, and science communicators use this skill to turn local or synthetic geospatial time-series data into a scroll-driven story map with narrative sections, embedded maps, charts, and a run manifest. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release includes under-disclosed credential and network helpers, including a hardcoded Earthdata password. <br>
Mitigation: Review the package before installation and prefer a build that removes hardcoded credentials and documents credential and network behavior. <br>
Risk: Helper code can read user-level credential files and make network requests if those helpers are used. <br>
Mitigation: Run the skill in a restricted environment, provide only required credentials, and avoid helper paths that are not needed for local story generation. <br>
Risk: Dependencies are not pinned in requirements.txt. <br>
Mitigation: Pin and review dependencies before deployment. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/ruiduobao/skills/geoskill-spatial-storytelling) <br>
- [README](artifact/README.md) <br>
- [Skill instructions](artifact/SKILL.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, HTML, JSON, GeoTIFF, Configuration] <br>
**Output Format:** [HTML story page, JSON chapter data, GeoTIFF stack, and JSON output manifest] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Synthetic mode can run offline; local GeoTIFF or vector inputs may be used when provided.] <br>

## Skill Version(s): <br>
1.0.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
